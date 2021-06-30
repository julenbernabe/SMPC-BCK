/*
Copyright (c) 2017, The University of Bristol, Senate House, Tyndall Avenue, Bristol, BS8 1TH, United Kingdom.
Copyright (c) 2020, COSIC-KU Leuven, Kasteelpark Arenberg 10, bus 2452, B-3001 Leuven-Heverlee, Belgium.

All rights reserved
*/

#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

#include "openssl/err.h"
#include "openssl/ssl.h"

#include "FHE/FHE_Keys.h"
#include "FHE/FHE_Params.h"
#include "GC/SimplifyCircuit.h"
#include "LSSS/Share.h"
#include "OT/aBitVector.h"
#include "config.h"

// Nada más pasamos por main(), ./Setup.x pasa por aquí. En este programa se inician los certificados 
// de cada player.

void init_certs()
{
  // Initialize the SSL library
  OPENSSL_init_ssl(
      OPENSSL_INIT_LOAD_SSL_STRINGS | OPENSSL_INIT_LOAD_CRYPTO_STRINGS, NULL);
  // SSL_CTX *ctx = InitServerCTX();

  ifstream input1 ("Data/NetworkData.txt");
  if (input1.fail())
    {
      throw file_error("Data/NetworkData.txt does not exist.");
    }
  
  string CAName;
  getline(input1,CAName);
    
  // string CAName = "RootCA";
  cout << CAName << endl;
  //cin >> CAName;

  string str= "Cert-Store/" + CAName;
  ifstream cert_file(str);
  if (cert_file.fail())
    {
      throw file_error(str);
    }
  
  // In the following commands we are proving that the CA has a valid certificate. After doing all that proccess we 
  // write in NetworkData.txt its certificate name for future calculations.

  stringstream cert_buff;
  cert_buff << cert_file.rdbuf();
  cout << cert_buff.str() << endl;
  BIO *bio_mem= BIO_new(BIO_s_mem());
  BIO_puts(bio_mem, cert_buff.str().c_str());
  X509 *x509= PEM_read_bio_X509(bio_mem, NULL, NULL, NULL);
  EVP_PKEY *pkey= X509_get_pubkey(x509);
  BIO_free(bio_mem);
  X509_free(x509);
  cert_file.close();

  // From now on, we have to prove that the players have provided valid certificates. We obtain such data from NetworkData1.txt
  // (which we suppose is the file provided by the networking proccess in Ethereum).

  unsigned int n, t, bd;
  input1  >> n;

  cout << "The network will be composed by " << n <<" players. For each player now enter:\n";
  cout << " * IP address\n";
  cout << " * Certificate\n";

  for (int i= 0; i < n; i++)
    {
      /* string mask = "10.10.10.10";
      cout << "\nPlayer " << i << "\n";
      cout << " * IP Address " << mask << i << endl; // A cada IP le anade al '10.10.10.10' un 0, 1, 2, 3,... dependiendo de qué player sea (0, 1, 2, 3...)
      //cin >> str;
      output << i << " " << mask << i << " "; // Aquí lo vuelca sobre DataNetwork.txt (es lo que hace el output)
      
      str = "Player" + to_string(i) + ".crt"; // Aquí configura los .crt de cada player y en el siguiente comando los vuelca a DataNetwork.txt
      cout << " * Certificate " << str << endl; 
      //cin >> str;
      output << str << " ";
      str = */
      string index;
      input1 >> index;
      string IP;
      input1 >> IP;
      string CRT;
      input1 >> CRT;
      string CN;
      input1 >> CN;
      str = "Cert-Store/" + CRT;
      ifstream player_cert_file(str);
      if (player_cert_file.fail())
        {
          throw file_error(str);
        }
      stringstream player_cert_buff;
      player_cert_buff << player_cert_file.rdbuf();
      cout << player_cert_buff.str() << endl;
      bio_mem= BIO_new(BIO_s_mem());
      BIO_puts(bio_mem, player_cert_buff.str().c_str());
      X509 *player_x509= PEM_read_bio_X509(bio_mem, NULL, NULL, NULL);
      char buffer[256];
      X509_NAME_get_text_by_NID(X509_get_subject_name(player_x509), NID_commonName, buffer, 256);
      cout << "Common name in certificate is " << buffer << endl; // En buffer se guarda el Common Name del player i (el correo electrónico)
      // output << buffer << endl;                                   Aquí lo volcamos también a DataNetwork.txt
      int j= 0;
      while (buffer[j] != 0)
        {
          if (buffer[j] == ' ')
            {
              cout << "Common name may not contain spaces" << endl;
              abort();
            }
          j++;
        }
      int fl= X509_verify(player_x509, pkey);
      if (fl == 0)
        {
          cout << "Cerfificate does not verify" << endl;
          abort();
        }
      X509_free(player_x509);
      BIO_free(bio_mem);
      player_cert_file.close();
    }
  EVP_PKEY_free(pkey);
  
  // Choose non-fake in both cases
  input1.close();
}

void init_secret_sharing()
{
  ifstream input1("Data/NetworkData.txt");
  if (input1.fail())
    {
      throw file_error("Data/NetworkData.txt does not exist.");
    }
  
  ifstream input2 ("Data/other_info.txt");
  if (input2.fail())
    {
      throw file_error("Data/other_info.txt does not exist.");
    }
  string RootCAPath;
  string infoPath;
  string bcPath;
  string schPath;
  string prepPath;
  bigint p;
  getline(input2,RootCAPath);
  getline(input2,infoPath);
  getline(input2,bcPath);
  getline(input2,schPath);
  getline(input2,prepPath);
  input2 >> p;

  string str;
  input1 >> str;       // En str se guarda ROOTCA.crt
  unsigned int n;
  input1 >> n;         // En n se guarda el número de jugadores, en este caso 3 por defecto (son los que hemos cogido en el anterior apartado)
  input1.close();
  input2.close();

  cout << "\nNumber of players = " << n << endl;

  cout << "\nUsing modulus p=" << p << endl;
  gfp::init_field(p);
  //}

  ShareData SD;
  
  int t = n / 2;
  
  cout << "\nUsing threshold t = " << t << endl;
  cout << "\nInitialising Linear Shamir Secret-Sharing\n";
    // SD ha sido llamado dentro de ShareData.cpp. SD.Initialize_Shamir(n,t) es un programa dentro de ShareData.cpp
  SD.Initialize_Shamir(n, t);   // A Shamir le hemos pasado el número de players... Sí afecta a SharingData.txt

  ifstream circuit1("src/Local/ConversionCircuit-LSSS_to_GC_1.txt");
  if (circuit1.fail())
    {
      throw file_error("src/Local/ConversionCircuit-LSSS_to_GC_1.txt");
    }
  bigint line1;
  circuit1 >> line1;
  string salto;
  getline(circuit1,salto);
  ifstream circuit2("src/Local/ConversionCircuit-LSSS_to_GC_2.txt");
  if (circuit2.fail())
    {
      throw file_error("src/Local/ConversionCircuit-LSSS_to_GC_2.txt");
    }
  bigint line2;
  circuit2 >> line2;
  getline(circuit2,salto);
  ifstream circuit3("src/Local/ConversionCircuit-LSSS_to_GC_3.txt");
  if (circuit3.fail())
    {
      throw file_error("src/Local/ConversionCircuit-LSSS_to_GC_3.txt");
    }
  bigint line3;
  circuit3 >> line3;   
  getline(circuit3,salto);
  ofstream out2("Data/ConversionCircuit-LSSS_to_GC.txt");
  if (out2.fail())
    {
      throw file_error("Data/ConversionCircuit-LSSS_to_GC.txt");
    }
  if (p == line1)
    {
      string line;
      while ( getline (circuit1,line) )
        {
          out2 << line << '\n';
        }
    }
  if (p == line2)
    {
      string line;
      while ( getline (circuit2,line) )
        {
          out2 << line << '\n';
        }
    }
  if (p == line3)
    {
      string line;
      while ( getline (circuit3,line) )
        {
          out2 << line << '\n';
        }
    }
  
  circuit1.close();
  circuit2.close();
  circuit3.close();
  out2.close();

  ofstream out("Data/SharingData.txt");
  if (out.fail())
    {
      throw file_error("Data/SharingData.txt");
    }
  out << p << endl;
  out << SD;
  out.close();

  PRNG G;
  G.ReSeed(0);
  for (unsigned int i= 0; i < n; i++)
    {
      stringstream ss;
      ss << "Data/MKey-" << i << ".key";
      ofstream outk(ss.str().c_str());
      if (outk.fail())
        {
          throw file_error(ss.str());
        }
      for (unsigned int j= 0; j < SD.nmacs; j++)
        {
          gfp aa;
          aa.randomize(G);
          outk << aa << " ";
        }
      outk << endl;
      outk.close();
    }

  cout << "Finished setting up secret sharing. \nThe underlying MSP is...\n"
       << SD.M << endl;
}

// El ./Setup.x empieza aquí. Argc es siempre 1, luego se imprime en pantalla "Setting up the environment...".
// Después, va directamente a ejecutar init_certs(), init_secret_sharing() e init_conversion().
int main(int argc, const char *argv[])
{
  int ans = 4;
  if (argc == 1)
    {
      cout << "\nSetting up the environment...\n"
           << endl;
    }
  else if (argc == 2)
    {
      ans= atoi(argv[1]);
      if (ans < 0 || ans > 4)
        {
          throw bad_value();
        }
    }

  init_certs();
  init_secret_sharing();
}
