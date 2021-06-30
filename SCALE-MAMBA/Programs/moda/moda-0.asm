# moda-0--0
ldint r0, 0 # 0
pushint r0 # 1
# moda-0-begin-loop-1
popint r1 # 2
ldint r2, 1048576 # 3
mulint r3, r1, r2 # 4
convint c0, r3 # 5
ldsi s1, 0 # 6
addm s0, s1, c0 # 7
ldint r4, 8192 # 8
addint r5, r1, r4 # 9
stmsi s0, r5 # 10
ldint r6, 1 # 11
addint r7, r1, r6 # 12
pushint r7 # 13
ldint r8, 5 # 14
ltint r9, r7, r8 # 15
jmpnz r9, -15 # 16
# moda-0-end-loop-2
popint r10 # 17
ldint r11, 0 # 18
pushint r11 # 19
# moda-0-begin-loop-3
popint r12 # 20
ldint r13, 2 # 21
mulint r14, r12, r13 # 22
ldint r15, 1048576 # 23
mulint r16, r14, r15 # 24
convint c1, r16 # 25
ldsi s3, 0 # 26
addm s2, s3, c1 # 27
ldint r17, 8197 # 28
addint r18, r12, r17 # 29
stmsi s2, r18 # 30
ldint r19, 1 # 31
addint r20, r12, r19 # 32
pushint r20 # 33
ldint r21, 5 # 34
ltint r22, r20, r21 # 35
jmpnz r22, -17 # 36
# moda-0-end-loop-4
popint r23 # 37
ldint r24, 0 # 38
pushint r24 # 39
# moda-0-begin-loop-5
popint r25 # 40
ldint r26, 8192 # 41
addint r27, r25, r26 # 42
ldmsi s4, r27 # 43
ldint r28, 8202 # 44
addint r29, r25, r28 # 45
stmsi s4, r29 # 46
ldint r30, 1 # 47
addint r31, r25, r30 # 48
pushint r31 # 49
ldint r32, 5 # 50
ltint r33, r31, r32 # 51
jmpnz r33, -13 # 52
# moda-0-end-loop-6
popint r34 # 53
ldint r35, 0 # 54
pushint r35 # 55
# moda-0-begin-loop-7
popint r36 # 56
ldint r37, 8197 # 57
addint r38, r36, r37 # 58
ldmsi s5, r38 # 59
ldint r39, 5 # 60
addint r40, r36, r39 # 61
ldint r41, 8202 # 62
addint r42, r40, r41 # 63
stmsi s5, r42 # 64
ldint r43, 1 # 65
addint r44, r36, r43 # 66
pushint r44 # 67
ldint r45, 5 # 68
ltint r46, r44, r45 # 69
jmpnz r46, -15 # 70
# moda-0-end-loop-8
popint r47 # 71
ldi c2, 0 # 72
stmc c2, 8192 # 73
ldint r48, 0 # 74
pushint r48 # 75
# moda-0-begin-loop-9
popint r49 # 76
ldint r50, 8202 # 77
addint r51, r49, r50 # 78
ldmsi s6, r51 # 79
ldi c3, 0 # 80
stmc c3, 8203 # 81
ldint r52, 0 # 82
pushint r52 # 83
# moda-0-begin-loop-10
popint r53 # 84
ldint r54, 8202 # 85
addint r55, r53, r54 # 86
ldmsi s7, r55 # 87
subs s8, s7, s6 # 88
bit s214 # 89
adds s135, s214, s214 # 90
bit s175 # 91
adds s215, s135, s175 # 92
adds s136, s215, s215 # 93
bit s176 # 94
adds s216, s136, s176 # 95
adds s137, s216, s216 # 96
bit s177 # 97
adds s217, s137, s177 # 98
adds s138, s217, s217 # 99
bit s178 # 100
adds s218, s138, s178 # 101
adds s139, s218, s218 # 102
bit s179 # 103
adds s219, s139, s179 # 104
adds s140, s219, s219 # 105
bit s180 # 106
adds s220, s140, s180 # 107
adds s141, s220, s220 # 108
bit s181 # 109
adds s221, s141, s181 # 110
adds s142, s221, s221 # 111
bit s182 # 112
adds s222, s142, s182 # 113
adds s143, s222, s222 # 114
bit s183 # 115
adds s223, s143, s183 # 116
adds s144, s223, s223 # 117
bit s184 # 118
adds s224, s144, s184 # 119
adds s145, s224, s224 # 120
bit s185 # 121
adds s225, s145, s185 # 122
adds s146, s225, s225 # 123
bit s186 # 124
adds s226, s146, s186 # 125
adds s147, s226, s226 # 126
bit s187 # 127
adds s227, s147, s187 # 128
adds s148, s227, s227 # 129
bit s188 # 130
adds s228, s148, s188 # 131
adds s149, s228, s228 # 132
bit s189 # 133
adds s229, s149, s189 # 134
adds s150, s229, s229 # 135
bit s190 # 136
adds s230, s150, s190 # 137
adds s151, s230, s230 # 138
bit s191 # 139
adds s231, s151, s191 # 140
adds s152, s231, s231 # 141
bit s192 # 142
adds s232, s152, s192 # 143
adds s153, s232, s232 # 144
bit s193 # 145
adds s233, s153, s193 # 146
adds s154, s233, s233 # 147
bit s194 # 148
adds s234, s154, s194 # 149
adds s155, s234, s234 # 150
bit s195 # 151
adds s235, s155, s195 # 152
adds s156, s235, s235 # 153
bit s196 # 154
adds s236, s156, s196 # 155
adds s157, s236, s236 # 156
bit s197 # 157
adds s237, s157, s197 # 158
adds s158, s237, s237 # 159
bit s198 # 160
adds s238, s158, s198 # 161
adds s159, s238, s238 # 162
bit s199 # 163
adds s239, s159, s199 # 164
adds s160, s239, s239 # 165
bit s200 # 166
adds s240, s160, s200 # 167
adds s161, s240, s240 # 168
bit s201 # 169
adds s241, s161, s201 # 170
adds s162, s241, s241 # 171
bit s202 # 172
adds s242, s162, s202 # 173
adds s163, s242, s242 # 174
bit s203 # 175
adds s243, s163, s203 # 176
adds s164, s243, s243 # 177
bit s204 # 178
adds s244, s164, s204 # 179
adds s165, s244, s244 # 180
bit s205 # 181
adds s245, s165, s205 # 182
adds s166, s245, s245 # 183
bit s206 # 184
adds s246, s166, s206 # 185
adds s167, s246, s246 # 186
bit s207 # 187
adds s247, s167, s207 # 188
adds s168, s247, s247 # 189
bit s208 # 190
adds s248, s168, s208 # 191
adds s169, s248, s248 # 192
bit s209 # 193
adds s249, s169, s209 # 194
adds s170, s249, s249 # 195
bit s210 # 196
adds s250, s170, s210 # 197
adds s171, s250, s250 # 198
bit s211 # 199
adds s251, s171, s211 # 200
adds s172, s251, s251 # 201
bit s212 # 202
adds s252, s172, s212 # 203
adds s173, s252, s252 # 204
bit s213 # 205
adds s9, s173, s213 # 206
bit s51 # 207
adds s54, s51, s51 # 208
bit s50 # 209
adds s55, s54, s50 # 210
adds s56, s55, s55 # 211
bit s49 # 212
adds s57, s56, s49 # 213
adds s58, s57, s57 # 214
bit s48 # 215
adds s59, s58, s48 # 216
adds s60, s59, s59 # 217
bit s47 # 218
adds s61, s60, s47 # 219
adds s62, s61, s61 # 220
bit s46 # 221
adds s63, s62, s46 # 222
adds s64, s63, s63 # 223
bit s45 # 224
adds s65, s64, s45 # 225
adds s66, s65, s65 # 226
bit s44 # 227
adds s67, s66, s44 # 228
adds s68, s67, s67 # 229
bit s43 # 230
adds s69, s68, s43 # 231
adds s70, s69, s69 # 232
bit s42 # 233
adds s71, s70, s42 # 234
adds s72, s71, s71 # 235
bit s41 # 236
adds s73, s72, s41 # 237
adds s74, s73, s73 # 238
bit s40 # 239
adds s75, s74, s40 # 240
adds s76, s75, s75 # 241
bit s39 # 242
adds s77, s76, s39 # 243
adds s78, s77, s77 # 244
bit s38 # 245
adds s79, s78, s38 # 246
adds s80, s79, s79 # 247
bit s37 # 248
adds s81, s80, s37 # 249
adds s82, s81, s81 # 250
bit s36 # 251
adds s83, s82, s36 # 252
adds s84, s83, s83 # 253
bit s35 # 254
adds s85, s84, s35 # 255
adds s86, s85, s85 # 256
bit s34 # 257
adds s87, s86, s34 # 258
adds s88, s87, s87 # 259
bit s33 # 260
adds s89, s88, s33 # 261
adds s90, s89, s89 # 262
bit s32 # 263
adds s91, s90, s32 # 264
adds s92, s91, s91 # 265
bit s31 # 266
adds s93, s92, s31 # 267
adds s94, s93, s93 # 268
bit s30 # 269
adds s95, s94, s30 # 270
adds s96, s95, s95 # 271
bit s29 # 272
adds s97, s96, s29 # 273
adds s98, s97, s97 # 274
bit s28 # 275
adds s99, s98, s28 # 276
adds s100, s99, s99 # 277
bit s27 # 278
adds s101, s100, s27 # 279
adds s102, s101, s101 # 280
bit s26 # 281
adds s103, s102, s26 # 282
adds s104, s103, s103 # 283
bit s25 # 284
adds s105, s104, s25 # 285
adds s106, s105, s105 # 286
bit s24 # 287
adds s107, s106, s24 # 288
adds s108, s107, s107 # 289
bit s23 # 290
adds s109, s108, s23 # 291
adds s110, s109, s109 # 292
bit s22 # 293
adds s111, s110, s22 # 294
adds s112, s111, s111 # 295
bit s21 # 296
adds s113, s112, s21 # 297
adds s114, s113, s113 # 298
bit s20 # 299
adds s115, s114, s20 # 300
adds s116, s115, s115 # 301
bit s19 # 302
adds s117, s116, s19 # 303
adds s118, s117, s117 # 304
bit s18 # 305
adds s119, s118, s18 # 306
adds s120, s119, s119 # 307
bit s17 # 308
adds s121, s120, s17 # 309
adds s122, s121, s121 # 310
bit s16 # 311
adds s123, s122, s16 # 312
adds s124, s123, s123 # 313
bit s15 # 314
adds s125, s124, s15 # 315
adds s126, s125, s125 # 316
bit s14 # 317
adds s127, s126, s14 # 318
adds s128, s127, s127 # 319
bit s13 # 320
adds s129, s128, s13 # 321
adds s130, s129, s129 # 322
bit s12 # 323
adds s131, s130, s12 # 324
adds s132, s131, s131 # 325
bit s11 # 326
adds s133, s132, s11 # 327
movs s10, s133 # 328
ldi c5, 1 # 329
shlci c6, c5, 31 # 330
mulci c7, c6, 1024 # 331
mulm s254, s9, c7 # 332
adds s255, s8, s254 # 333
adds s256, s255, s10 # 334
startopen 1, s256 # 335
stopopen 1, c4 # 336
modci c91, c4, 2 # 337
subc c10, c4, c91 # 338
divci c51, c10, 2 # 339
modci c92, c51, 2 # 340
subc c11, c51, c92 # 341
divci c52, c11, 2 # 342
modci c93, c52, 2 # 343
subc c12, c52, c93 # 344
divci c53, c12, 2 # 345
modci c94, c53, 2 # 346
subc c13, c53, c94 # 347
divci c54, c13, 2 # 348
modci c95, c54, 2 # 349
subc c14, c54, c95 # 350
divci c55, c14, 2 # 351
modci c96, c55, 2 # 352
subc c15, c55, c96 # 353
divci c56, c15, 2 # 354
modci c97, c56, 2 # 355
subc c16, c56, c97 # 356
divci c57, c16, 2 # 357
modci c98, c57, 2 # 358
subc c17, c57, c98 # 359
divci c58, c17, 2 # 360
modci c99, c58, 2 # 361
subc c18, c58, c99 # 362
divci c59, c18, 2 # 363
modci c100, c59, 2 # 364
subc c19, c59, c100 # 365
divci c60, c19, 2 # 366
modci c101, c60, 2 # 367
subc c20, c60, c101 # 368
divci c61, c20, 2 # 369
modci c102, c61, 2 # 370
subc c21, c61, c102 # 371
divci c62, c21, 2 # 372
modci c103, c62, 2 # 373
subc c22, c62, c103 # 374
divci c63, c22, 2 # 375
modci c104, c63, 2 # 376
subc c23, c63, c104 # 377
divci c64, c23, 2 # 378
modci c105, c64, 2 # 379
subc c24, c64, c105 # 380
divci c65, c24, 2 # 381
modci c106, c65, 2 # 382
subc c25, c65, c106 # 383
divci c66, c25, 2 # 384
modci c107, c66, 2 # 385
subc c26, c66, c107 # 386
divci c67, c26, 2 # 387
modci c108, c67, 2 # 388
subc c27, c67, c108 # 389
divci c68, c27, 2 # 390
modci c109, c68, 2 # 391
subc c28, c68, c109 # 392
divci c69, c28, 2 # 393
modci c110, c69, 2 # 394
subc c29, c69, c110 # 395
divci c70, c29, 2 # 396
modci c111, c70, 2 # 397
subc c30, c70, c111 # 398
divci c71, c30, 2 # 399
modci c112, c71, 2 # 400
subc c31, c71, c112 # 401
divci c72, c31, 2 # 402
modci c113, c72, 2 # 403
subc c32, c72, c113 # 404
divci c73, c32, 2 # 405
modci c114, c73, 2 # 406
subc c33, c73, c114 # 407
divci c74, c33, 2 # 408
modci c115, c74, 2 # 409
subc c34, c74, c115 # 410
divci c75, c34, 2 # 411
modci c116, c75, 2 # 412
subc c35, c75, c116 # 413
divci c76, c35, 2 # 414
modci c117, c76, 2 # 415
subc c36, c76, c117 # 416
divci c77, c36, 2 # 417
modci c118, c77, 2 # 418
subc c37, c77, c118 # 419
divci c78, c37, 2 # 420
modci c119, c78, 2 # 421
subc c38, c78, c119 # 422
divci c79, c38, 2 # 423
modci c120, c79, 2 # 424
subc c39, c79, c120 # 425
divci c80, c39, 2 # 426
modci c121, c80, 2 # 427
subc c40, c80, c121 # 428
divci c81, c40, 2 # 429
modci c122, c81, 2 # 430
subc c41, c81, c122 # 431
divci c82, c41, 2 # 432
modci c123, c82, 2 # 433
subc c42, c82, c123 # 434
divci c83, c42, 2 # 435
modci c124, c83, 2 # 436
subc c43, c83, c124 # 437
divci c84, c43, 2 # 438
modci c125, c84, 2 # 439
subc c44, c84, c125 # 440
divci c85, c44, 2 # 441
modci c126, c85, 2 # 442
subc c45, c85, c126 # 443
divci c86, c45, 2 # 444
modci c127, c86, 2 # 445
subc c46, c86, c127 # 446
divci c87, c46, 2 # 447
modci c128, c87, 2 # 448
subc c47, c87, c128 # 449
divci c88, c47, 2 # 450
modci c129, c88, 2 # 451
subc c48, c88, c129 # 452
divci c89, c48, 2 # 453
modci c130, c89, 2 # 454
subc c49, c89, c130 # 455
divci c90, c49, 2 # 456
modci c131, c90, 2 # 457
addm s257, s11, c91 # 458
mulci c133, c91, 2 # 459
mulm s258, s11, c133 # 460
subs s259, s257, s258 # 461
addm s260, s12, c92 # 462
mulci c136, c92, 2 # 463
mulm s261, s12, c136 # 464
subs s262, s260, s261 # 465
addm s263, s13, c93 # 466
mulci c139, c93, 2 # 467
mulm s264, s13, c139 # 468
subs s265, s263, s264 # 469
addm s266, s14, c94 # 470
mulci c142, c94, 2 # 471
mulm s267, s14, c142 # 472
subs s268, s266, s267 # 473
addm s269, s15, c95 # 474
mulci c145, c95, 2 # 475
mulm s270, s15, c145 # 476
subs s271, s269, s270 # 477
addm s272, s16, c96 # 478
mulci c148, c96, 2 # 479
mulm s273, s16, c148 # 480
subs s274, s272, s273 # 481
addm s275, s17, c97 # 482
mulci c151, c97, 2 # 483
mulm s276, s17, c151 # 484
subs s277, s275, s276 # 485
addm s278, s18, c98 # 486
mulci c154, c98, 2 # 487
mulm s279, s18, c154 # 488
subs s280, s278, s279 # 489
addm s281, s19, c99 # 490
mulci c157, c99, 2 # 491
mulm s282, s19, c157 # 492
subs s283, s281, s282 # 493
addm s284, s20, c100 # 494
mulci c160, c100, 2 # 495
mulm s285, s20, c160 # 496
subs s286, s284, s285 # 497
addm s287, s21, c101 # 498
mulci c163, c101, 2 # 499
mulm s288, s21, c163 # 500
subs s289, s287, s288 # 501
addm s290, s22, c102 # 502
mulci c166, c102, 2 # 503
mulm s291, s22, c166 # 504
subs s292, s290, s291 # 505
addm s293, s23, c103 # 506
mulci c169, c103, 2 # 507
mulm s294, s23, c169 # 508
subs s295, s293, s294 # 509
addm s296, s24, c104 # 510
mulci c172, c104, 2 # 511
mulm s297, s24, c172 # 512
subs s298, s296, s297 # 513
addm s299, s25, c105 # 514
mulci c175, c105, 2 # 515
mulm s300, s25, c175 # 516
subs s301, s299, s300 # 517
addm s302, s26, c106 # 518
mulci c178, c106, 2 # 519
mulm s303, s26, c178 # 520
subs s304, s302, s303 # 521
addm s305, s27, c107 # 522
mulci c181, c107, 2 # 523
mulm s306, s27, c181 # 524
subs s307, s305, s306 # 525
addm s308, s28, c108 # 526
mulci c184, c108, 2 # 527
mulm s309, s28, c184 # 528
subs s310, s308, s309 # 529
addm s311, s29, c109 # 530
mulci c187, c109, 2 # 531
mulm s312, s29, c187 # 532
subs s313, s311, s312 # 533
addm s314, s30, c110 # 534
mulci c190, c110, 2 # 535
mulm s315, s30, c190 # 536
subs s316, s314, s315 # 537
addm s317, s31, c111 # 538
mulci c193, c111, 2 # 539
mulm s318, s31, c193 # 540
subs s319, s317, s318 # 541
addm s320, s32, c112 # 542
mulci c196, c112, 2 # 543
mulm s321, s32, c196 # 544
subs s322, s320, s321 # 545
addm s323, s33, c113 # 546
mulci c199, c113, 2 # 547
mulm s324, s33, c199 # 548
subs s325, s323, s324 # 549
addm s326, s34, c114 # 550
mulci c202, c114, 2 # 551
mulm s327, s34, c202 # 552
subs s328, s326, s327 # 553
addm s329, s35, c115 # 554
mulci c205, c115, 2 # 555
mulm s330, s35, c205 # 556
subs s331, s329, s330 # 557
addm s332, s36, c116 # 558
mulci c208, c116, 2 # 559
mulm s333, s36, c208 # 560
subs s334, s332, s333 # 561
addm s335, s37, c117 # 562
mulci c211, c117, 2 # 563
mulm s336, s37, c211 # 564
subs s337, s335, s336 # 565
addm s338, s38, c118 # 566
mulci c214, c118, 2 # 567
mulm s339, s38, c214 # 568
subs s340, s338, s339 # 569
addm s341, s39, c119 # 570
mulci c217, c119, 2 # 571
mulm s342, s39, c217 # 572
subs s343, s341, s342 # 573
addm s344, s40, c120 # 574
mulci c220, c120, 2 # 575
mulm s345, s40, c220 # 576
subs s346, s344, s345 # 577
addm s347, s41, c121 # 578
mulci c223, c121, 2 # 579
mulm s348, s41, c223 # 580
subs s349, s347, s348 # 581
addm s350, s42, c122 # 582
mulci c226, c122, 2 # 583
mulm s351, s42, c226 # 584
subs s352, s350, s351 # 585
addm s353, s43, c123 # 586
mulci c229, c123, 2 # 587
mulm s354, s43, c229 # 588
subs s355, s353, s354 # 589
addm s356, s44, c124 # 590
mulci c232, c124, 2 # 591
mulm s357, s44, c232 # 592
subs s358, s356, s357 # 593
addm s359, s45, c125 # 594
mulci c235, c125, 2 # 595
mulm s360, s45, c235 # 596
subs s361, s359, s360 # 597
addm s362, s46, c126 # 598
mulci c238, c126, 2 # 599
mulm s363, s46, c238 # 600
subs s364, s362, s363 # 601
addm s365, s47, c127 # 602
mulci c241, c127, 2 # 603
mulm s366, s47, c241 # 604
subs s367, s365, s366 # 605
addm s368, s48, c128 # 606
mulci c244, c128, 2 # 607
mulm s369, s48, c244 # 608
subs s370, s368, s369 # 609
addm s371, s49, c129 # 610
mulci c247, c129, 2 # 611
mulm s372, s49, c247 # 612
subs s373, s371, s372 # 613
addm s374, s50, c130 # 614
mulci c250, c130, 2 # 615
mulm s375, s50, c250 # 616
subs s376, s374, s375 # 617
addm s377, s51, c131 # 618
mulci c253, c131, 2 # 619
mulm s378, s51, c253 # 620
subs s379, s377, s378 # 621
adds s380, s259, s262 # 622
triple s382, s383, s384 # 623
subs s385, s259, s382 # 624
subs s386, s262, s383 # 625
startopen 2, s385, s386 # 626
stopopen 2, c255, c256 # 627
mulm s387, s383, c255 # 628
mulm s388, s382, c256 # 629
mulc c257, c255, c256 # 630
adds s389, s384, s387 # 631
adds s390, s389, s388 # 632
addm s381, s390, c257 # 633
subs s391, s380, s381 # 634
adds s392, s268, s271 # 635
triple s394, s395, s396 # 636
subs s397, s268, s394 # 637
subs s398, s271, s395 # 638
startopen 2, s397, s398 # 639
stopopen 2, c258, c259 # 640
mulm s399, s395, c258 # 641
mulm s400, s394, c259 # 642
mulc c260, c258, c259 # 643
adds s401, s396, s399 # 644
adds s402, s401, s400 # 645
addm s393, s402, c260 # 646
subs s403, s392, s393 # 647
adds s404, s265, s403 # 648
triple s406, s407, s408 # 649
subs s409, s265, s406 # 650
subs s410, s403, s407 # 651
startopen 2, s409, s410 # 652
stopopen 2, c261, c262 # 653
mulm s411, s407, c261 # 654
mulm s412, s406, c262 # 655
mulc c263, c261, c262 # 656
adds s413, s408, s411 # 657
adds s414, s413, s412 # 658
addm s405, s414, c263 # 659
subs s415, s404, s405 # 660
adds s416, s391, s415 # 661
triple s418, s419, s420 # 662
subs s421, s391, s418 # 663
subs s422, s415, s419 # 664
startopen 2, s421, s422 # 665
stopopen 2, c264, c265 # 666
mulm s423, s419, c264 # 667
mulm s424, s418, c265 # 668
mulc c266, c264, c265 # 669
adds s425, s420, s423 # 670
adds s426, s425, s424 # 671
addm s417, s426, c266 # 672
subs s427, s416, s417 # 673
adds s428, s274, s277 # 674
triple s430, s431, s432 # 675
subs s433, s274, s430 # 676
subs s434, s277, s431 # 677
startopen 2, s433, s434 # 678
stopopen 2, c267, c268 # 679
mulm s435, s431, c267 # 680
mulm s436, s430, c268 # 681
mulc c269, c267, c268 # 682
adds s437, s432, s435 # 683
adds s438, s437, s436 # 684
addm s429, s438, c269 # 685
subs s439, s428, s429 # 686
adds s440, s283, s286 # 687
triple s442, s443, s444 # 688
subs s445, s283, s442 # 689
subs s446, s286, s443 # 690
startopen 2, s445, s446 # 691
stopopen 2, c270, c271 # 692
mulm s447, s443, c270 # 693
mulm s448, s442, c271 # 694
mulc c272, c270, c271 # 695
adds s449, s444, s447 # 696
adds s450, s449, s448 # 697
addm s441, s450, c272 # 698
subs s451, s440, s441 # 699
adds s452, s280, s451 # 700
triple s454, s455, s456 # 701
subs s457, s280, s454 # 702
subs s458, s451, s455 # 703
startopen 2, s457, s458 # 704
stopopen 2, c273, c274 # 705
mulm s459, s455, c273 # 706
mulm s460, s454, c274 # 707
mulc c275, c273, c274 # 708
adds s461, s456, s459 # 709
adds s462, s461, s460 # 710
addm s453, s462, c275 # 711
subs s463, s452, s453 # 712
adds s464, s439, s463 # 713
triple s466, s467, s468 # 714
subs s469, s439, s466 # 715
subs s470, s463, s467 # 716
startopen 2, s469, s470 # 717
stopopen 2, c276, c277 # 718
mulm s471, s467, c276 # 719
mulm s472, s466, c277 # 720
mulc c278, c276, c277 # 721
adds s473, s468, s471 # 722
adds s474, s473, s472 # 723
addm s465, s474, c278 # 724
subs s475, s464, s465 # 725
adds s476, s427, s475 # 726
triple s478, s479, s480 # 727
subs s481, s427, s478 # 728
subs s482, s475, s479 # 729
startopen 2, s481, s482 # 730
stopopen 2, c279, c280 # 731
mulm s483, s479, c279 # 732
mulm s484, s478, c280 # 733
mulc c281, c279, c280 # 734
adds s485, s480, s483 # 735
adds s486, s485, s484 # 736
addm s477, s486, c281 # 737
subs s487, s476, s477 # 738
adds s488, s289, s292 # 739
triple s490, s491, s492 # 740
subs s493, s289, s490 # 741
subs s494, s292, s491 # 742
startopen 2, s493, s494 # 743
stopopen 2, c282, c283 # 744
mulm s495, s491, c282 # 745
mulm s496, s490, c283 # 746
mulc c284, c282, c283 # 747
adds s497, s492, s495 # 748
adds s498, s497, s496 # 749
addm s489, s498, c284 # 750
subs s499, s488, s489 # 751
adds s500, s298, s301 # 752
triple s502, s503, s504 # 753
subs s505, s298, s502 # 754
subs s506, s301, s503 # 755
startopen 2, s505, s506 # 756
stopopen 2, c285, c286 # 757
mulm s507, s503, c285 # 758
mulm s508, s502, c286 # 759
mulc c287, c285, c286 # 760
adds s509, s504, s507 # 761
adds s510, s509, s508 # 762
addm s501, s510, c287 # 763
subs s511, s500, s501 # 764
adds s512, s295, s511 # 765
triple s514, s515, s516 # 766
subs s517, s295, s514 # 767
subs s518, s511, s515 # 768
startopen 2, s517, s518 # 769
stopopen 2, c288, c289 # 770
mulm s519, s515, c288 # 771
mulm s520, s514, c289 # 772
mulc c290, c288, c289 # 773
adds s521, s516, s519 # 774
adds s522, s521, s520 # 775
addm s513, s522, c290 # 776
subs s523, s512, s513 # 777
adds s524, s499, s523 # 778
triple s526, s527, s528 # 779
subs s529, s499, s526 # 780
subs s530, s523, s527 # 781
startopen 2, s529, s530 # 782
stopopen 2, c291, c292 # 783
mulm s531, s527, c291 # 784
mulm s532, s526, c292 # 785
mulc c293, c291, c292 # 786
adds s533, s528, s531 # 787
adds s534, s533, s532 # 788
addm s525, s534, c293 # 789
subs s535, s524, s525 # 790
adds s536, s304, s307 # 791
triple s538, s539, s540 # 792
subs s541, s304, s538 # 793
subs s542, s307, s539 # 794
startopen 2, s541, s542 # 795
stopopen 2, c294, c295 # 796
mulm s543, s539, c294 # 797
mulm s544, s538, c295 # 798
mulc c296, c294, c295 # 799
adds s545, s540, s543 # 800
adds s546, s545, s544 # 801
addm s537, s546, c296 # 802
subs s547, s536, s537 # 803
adds s548, s313, s316 # 804
triple s550, s551, s552 # 805
subs s553, s313, s550 # 806
subs s554, s316, s551 # 807
startopen 2, s553, s554 # 808
stopopen 2, c297, c298 # 809
mulm s555, s551, c297 # 810
mulm s556, s550, c298 # 811
mulc c299, c297, c298 # 812
adds s557, s552, s555 # 813
adds s558, s557, s556 # 814
addm s549, s558, c299 # 815
subs s559, s548, s549 # 816
adds s560, s310, s559 # 817
triple s562, s563, s564 # 818
subs s565, s310, s562 # 819
subs s566, s559, s563 # 820
startopen 2, s565, s566 # 821
stopopen 2, c300, c301 # 822
mulm s567, s563, c300 # 823
mulm s568, s562, c301 # 824
mulc c302, c300, c301 # 825
adds s569, s564, s567 # 826
adds s570, s569, s568 # 827
addm s561, s570, c302 # 828
subs s571, s560, s561 # 829
adds s572, s547, s571 # 830
triple s574, s575, s576 # 831
subs s577, s547, s574 # 832
subs s578, s571, s575 # 833
startopen 2, s577, s578 # 834
stopopen 2, c303, c304 # 835
mulm s579, s575, c303 # 836
mulm s580, s574, c304 # 837
mulc c305, c303, c304 # 838
adds s581, s576, s579 # 839
adds s582, s581, s580 # 840
addm s573, s582, c305 # 841
subs s583, s572, s573 # 842
adds s584, s535, s583 # 843
triple s586, s587, s588 # 844
subs s589, s535, s586 # 845
subs s590, s583, s587 # 846
startopen 2, s589, s590 # 847
stopopen 2, c306, c307 # 848
mulm s591, s587, c306 # 849
mulm s592, s586, c307 # 850
mulc c308, c306, c307 # 851
adds s593, s588, s591 # 852
adds s594, s593, s592 # 853
addm s585, s594, c308 # 854
subs s595, s584, s585 # 855
adds s596, s487, s595 # 856
triple s598, s599, s600 # 857
subs s601, s487, s598 # 858
subs s602, s595, s599 # 859
startopen 2, s601, s602 # 860
stopopen 2, c309, c310 # 861
mulm s603, s599, c309 # 862
mulm s604, s598, c310 # 863
mulc c311, c309, c310 # 864
adds s605, s600, s603 # 865
adds s606, s605, s604 # 866
addm s597, s606, c311 # 867
subs s607, s596, s597 # 868
adds s608, s319, s322 # 869
triple s610, s611, s612 # 870
subs s613, s319, s610 # 871
subs s614, s322, s611 # 872
startopen 2, s613, s614 # 873
stopopen 2, c312, c313 # 874
mulm s615, s611, c312 # 875
mulm s616, s610, c313 # 876
mulc c314, c312, c313 # 877
adds s617, s612, s615 # 878
adds s618, s617, s616 # 879
addm s609, s618, c314 # 880
subs s619, s608, s609 # 881
adds s620, s328, s331 # 882
triple s622, s623, s624 # 883
subs s625, s328, s622 # 884
subs s626, s331, s623 # 885
startopen 2, s625, s626 # 886
stopopen 2, c315, c316 # 887
mulm s627, s623, c315 # 888
mulm s628, s622, c316 # 889
mulc c317, c315, c316 # 890
adds s629, s624, s627 # 891
adds s630, s629, s628 # 892
addm s621, s630, c317 # 893
subs s631, s620, s621 # 894
adds s632, s325, s631 # 895
triple s634, s635, s636 # 896
subs s637, s325, s634 # 897
subs s638, s631, s635 # 898
startopen 2, s637, s638 # 899
stopopen 2, c318, c319 # 900
mulm s639, s635, c318 # 901
mulm s640, s634, c319 # 902
mulc c320, c318, c319 # 903
adds s641, s636, s639 # 904
adds s642, s641, s640 # 905
addm s633, s642, c320 # 906
subs s643, s632, s633 # 907
adds s644, s619, s643 # 908
triple s646, s647, s648 # 909
subs s649, s619, s646 # 910
subs s650, s643, s647 # 911
startopen 2, s649, s650 # 912
stopopen 2, c321, c322 # 913
mulm s651, s647, c321 # 914
mulm s652, s646, c322 # 915
mulc c323, c321, c322 # 916
adds s653, s648, s651 # 917
adds s654, s653, s652 # 918
addm s645, s654, c323 # 919
subs s655, s644, s645 # 920
adds s656, s334, s337 # 921
triple s658, s659, s660 # 922
subs s661, s334, s658 # 923
subs s662, s337, s659 # 924
startopen 2, s661, s662 # 925
stopopen 2, c324, c325 # 926
mulm s663, s659, c324 # 927
mulm s664, s658, c325 # 928
mulc c326, c324, c325 # 929
adds s665, s660, s663 # 930
adds s666, s665, s664 # 931
addm s657, s666, c326 # 932
subs s667, s656, s657 # 933
adds s668, s343, s346 # 934
triple s670, s671, s672 # 935
subs s673, s343, s670 # 936
subs s674, s346, s671 # 937
startopen 2, s673, s674 # 938
stopopen 2, c327, c328 # 939
mulm s675, s671, c327 # 940
mulm s676, s670, c328 # 941
mulc c329, c327, c328 # 942
adds s677, s672, s675 # 943
adds s678, s677, s676 # 944
addm s669, s678, c329 # 945
subs s679, s668, s669 # 946
adds s680, s340, s679 # 947
triple s682, s683, s684 # 948
subs s685, s340, s682 # 949
subs s686, s679, s683 # 950
startopen 2, s685, s686 # 951
stopopen 2, c330, c331 # 952
mulm s687, s683, c330 # 953
mulm s688, s682, c331 # 954
mulc c332, c330, c331 # 955
adds s689, s684, s687 # 956
adds s690, s689, s688 # 957
addm s681, s690, c332 # 958
subs s691, s680, s681 # 959
adds s692, s667, s691 # 960
triple s694, s695, s696 # 961
subs s697, s667, s694 # 962
subs s698, s691, s695 # 963
startopen 2, s697, s698 # 964
stopopen 2, c333, c334 # 965
mulm s699, s695, c333 # 966
mulm s700, s694, c334 # 967
mulc c335, c333, c334 # 968
adds s701, s696, s699 # 969
adds s702, s701, s700 # 970
addm s693, s702, c335 # 971
subs s703, s692, s693 # 972
adds s704, s655, s703 # 973
triple s706, s707, s708 # 974
subs s709, s655, s706 # 975
subs s710, s703, s707 # 976
startopen 2, s709, s710 # 977
stopopen 2, c336, c337 # 978
mulm s711, s707, c336 # 979
mulm s712, s706, c337 # 980
mulc c338, c336, c337 # 981
adds s713, s708, s711 # 982
adds s714, s713, s712 # 983
addm s705, s714, c338 # 984
subs s715, s704, s705 # 985
adds s716, s349, s352 # 986
triple s718, s719, s720 # 987
subs s721, s349, s718 # 988
subs s722, s352, s719 # 989
startopen 2, s721, s722 # 990
stopopen 2, c339, c340 # 991
mulm s723, s719, c339 # 992
mulm s724, s718, c340 # 993
mulc c341, c339, c340 # 994
adds s725, s720, s723 # 995
adds s726, s725, s724 # 996
addm s717, s726, c341 # 997
subs s727, s716, s717 # 998
adds s728, s358, s361 # 999
triple s730, s731, s732 # 1000
subs s733, s358, s730 # 1001
subs s734, s361, s731 # 1002
startopen 2, s733, s734 # 1003
stopopen 2, c342, c343 # 1004
mulm s735, s731, c342 # 1005
mulm s736, s730, c343 # 1006
mulc c344, c342, c343 # 1007
adds s737, s732, s735 # 1008
adds s738, s737, s736 # 1009
addm s729, s738, c344 # 1010
subs s739, s728, s729 # 1011
adds s740, s355, s739 # 1012
triple s742, s743, s744 # 1013
subs s745, s355, s742 # 1014
subs s746, s739, s743 # 1015
startopen 2, s745, s746 # 1016
stopopen 2, c345, c346 # 1017
mulm s747, s743, c345 # 1018
mulm s748, s742, c346 # 1019
mulc c347, c345, c346 # 1020
adds s749, s744, s747 # 1021
adds s750, s749, s748 # 1022
addm s741, s750, c347 # 1023
subs s751, s740, s741 # 1024
adds s752, s727, s751 # 1025
triple s754, s755, s756 # 1026
subs s757, s727, s754 # 1027
subs s758, s751, s755 # 1028
startopen 2, s757, s758 # 1029
stopopen 2, c348, c349 # 1030
mulm s759, s755, c348 # 1031
mulm s760, s754, c349 # 1032
mulc c350, c348, c349 # 1033
adds s761, s756, s759 # 1034
adds s762, s761, s760 # 1035
addm s753, s762, c350 # 1036
subs s763, s752, s753 # 1037
adds s764, s367, s370 # 1038
triple s766, s767, s768 # 1039
subs s769, s367, s766 # 1040
subs s770, s370, s767 # 1041
startopen 2, s769, s770 # 1042
stopopen 2, c351, c352 # 1043
mulm s771, s767, c351 # 1044
mulm s772, s766, c352 # 1045
mulc c353, c351, c352 # 1046
adds s773, s768, s771 # 1047
adds s774, s773, s772 # 1048
addm s765, s774, c353 # 1049
subs s775, s764, s765 # 1050
adds s776, s364, s775 # 1051
triple s778, s779, s780 # 1052
subs s781, s364, s778 # 1053
subs s782, s775, s779 # 1054
startopen 2, s781, s782 # 1055
stopopen 2, c354, c355 # 1056
mulm s783, s779, c354 # 1057
mulm s784, s778, c355 # 1058
mulc c356, c354, c355 # 1059
adds s785, s780, s783 # 1060
adds s786, s785, s784 # 1061
addm s777, s786, c356 # 1062
subs s787, s776, s777 # 1063
adds s788, s376, s379 # 1064
triple s790, s791, s792 # 1065
subs s793, s376, s790 # 1066
subs s794, s379, s791 # 1067
startopen 2, s793, s794 # 1068
stopopen 2, c357, c358 # 1069
mulm s795, s791, c357 # 1070
mulm s796, s790, c358 # 1071
mulc c359, c357, c358 # 1072
adds s797, s792, s795 # 1073
adds s798, s797, s796 # 1074
addm s789, s798, c359 # 1075
subs s799, s788, s789 # 1076
adds s800, s373, s799 # 1077
triple s802, s803, s804 # 1078
subs s805, s373, s802 # 1079
subs s806, s799, s803 # 1080
startopen 2, s805, s806 # 1081
stopopen 2, c360, c361 # 1082
mulm s807, s803, c360 # 1083
mulm s808, s802, c361 # 1084
mulc c362, c360, c361 # 1085
adds s809, s804, s807 # 1086
adds s810, s809, s808 # 1087
addm s801, s810, c362 # 1088
subs s811, s800, s801 # 1089
adds s812, s787, s811 # 1090
triple s814, s815, s816 # 1091
subs s817, s787, s814 # 1092
subs s818, s811, s815 # 1093
startopen 2, s817, s818 # 1094
stopopen 2, c363, c364 # 1095
mulm s819, s815, c363 # 1096
mulm s820, s814, c364 # 1097
mulc c365, c363, c364 # 1098
adds s821, s816, s819 # 1099
adds s822, s821, s820 # 1100
addm s813, s822, c365 # 1101
subs s823, s812, s813 # 1102
adds s824, s763, s823 # 1103
triple s826, s827, s828 # 1104
subs s829, s763, s826 # 1105
subs s830, s823, s827 # 1106
startopen 2, s829, s830 # 1107
stopopen 2, c366, c367 # 1108
mulm s831, s827, c366 # 1109
mulm s832, s826, c367 # 1110
mulc c368, c366, c367 # 1111
adds s833, s828, s831 # 1112
adds s834, s833, s832 # 1113
addm s825, s834, c368 # 1114
subs s835, s824, s825 # 1115
adds s836, s715, s835 # 1116
triple s838, s839, s840 # 1117
subs s841, s715, s838 # 1118
subs s842, s835, s839 # 1119
startopen 2, s841, s842 # 1120
stopopen 2, c369, c370 # 1121
mulm s843, s839, c369 # 1122
mulm s844, s838, c370 # 1123
mulc c371, c369, c370 # 1124
adds s845, s840, s843 # 1125
adds s846, s845, s844 # 1126
addm s837, s846, c371 # 1127
subs s847, s836, s837 # 1128
adds s848, s607, s847 # 1129
triple s850, s851, s852 # 1130
subs s853, s607, s850 # 1131
subs s854, s847, s851 # 1132
startopen 2, s853, s854 # 1133
stopopen 2, c372, c373 # 1134
mulm s855, s851, c372 # 1135
mulm s856, s850, c373 # 1136
mulc c374, c372, c373 # 1137
adds s857, s852, s855 # 1138
adds s858, s857, s856 # 1139
addm s849, s858, c374 # 1140
subs s859, s848, s849 # 1141
subsfi s860, s859, 1 # 1142
startopen 1, s860 # 1143
stopopen 1, c375 # 1144
convmodp r56, c375, 64 # 1145
ldint r57, 1 # 1146
eqint r58, r56, r57 # 1147
jmpeqz r58, 4 # 1148
# moda-0-if-block-11
ldmc c376, 8203 # 1149
addci c377, c376, 1 # 1150
stmc c377, 8203 # 1151
jmp 3 # 1152
# moda-0-else-block-12
ldmc c378, 8203 # 1153
stmc c378, 8203 # 1154
stmc c378, 8203 # 1155
# moda-0-end-if-13
ldint r59, 1 # 1156
addint r60, r53, r59 # 1157
pushint r60 # 1158
ldint r61, 10 # 1159
ltint r62, r60, r61 # 1160
jmpnz r62, -1078 # 1161
# moda-0-end-loop-14
ldmc c379, 8203 # 1162
ldint r64, 8193 # 1163
addint r65, r49, r64 # 1164
stmci c379, r65 # 1165
ldmc c380, 8192 # 1166
convmodp r66, c379, 64 # 1167
convmodp r67, c380, 64 # 1168
gtint r68, r66, r67 # 1169
jmpeqz r68, 3 # 1170
# moda-0-if-block-15
ldmc c381, 8203 # 1171
stmc c381, 8192 # 1172
jmp 2 # 1173
# moda-0-else-block-16
ldmc c382, 8192 # 1174
stmc c382, 8192 # 1175
# moda-0-end-if-17
ldint r69, 1 # 1176
addint r70, r49, r69 # 1177
pushint r70 # 1178
ldint r71, 10 # 1179
ltint r72, r70, r71 # 1180
jmpnz r72, -1106 # 1181
# moda-0-end-loop-18
popint r73 # 1182
ldint r74, 0 # 1183
pushint r74 # 1184
# moda-0-begin-loop-19
popint r75 # 1185
ldint r76, 8202 # 1186
addint r77, r75, r76 # 1187
ldmsi s861, r77 # 1188
ldint r78, 8193 # 1189
addint r79, r75, r78 # 1190
ldmci c384, r79 # 1191
ldmc c385, 8192 # 1192
convmodp r80, c385, 64 # 1193
convmodp r81, c384, 64 # 1194
eqint r82, r80, r81 # 1195
jmpeqz r82, 4 # 1196
# moda-0-if-block-20
ldint r83, 8212 # 1197
addint r84, r75, r83 # 1198
stmsi s861, r84 # 1199
jmp 4 # 1200
# moda-0-else-block-21
ldsi s862, 0 # 1201
ldint r85, 8212 # 1202
addint r86, r75, r85 # 1203
stmsi s862, r86 # 1204
# moda-0-end-if-22
ldint r87, 1 # 1205
addint r88, r75, r87 # 1206
pushint r88 # 1207
ldint r89, 10 # 1208
ltint r90, r88, r89 # 1209
jmpnz r90, -26 # 1210
# moda-0-end-loop-23
popint r91 # 1211
print_char4 1330842122 # 1212
print_char4 1229149516 # 1213
print_char4 171593295 # 1214
print_char4 1830838604 # 1215
print_char4 677471343 # 1216
print_char4 1701864818 # 1217
print_char4 1633970548 # 1218
print_char4 1869488169 # 1219
print_char4 544433440 # 1220
print_char4 1981836917 # 1221
print_char4 1919904865 # 1222
print_char4 1768846624 # 1223
print_char 99 # 1224
print_char 111 # 1225
print_char 58 # 1226
print_char 10 # 1227
ldint r92, 0 # 1228
pushint r92 # 1229
# moda-0-begin-loop-24
popint r93 # 1230
ldint r94, 8212 # 1231
addint r95, r93, r94 # 1232
ldmsi s863, r95 # 1233
startopen 1, s863 # 1234
stopopen 1, c386 # 1235
movc c387, c386 # 1236
print_fix c387, 20, 41 # 1237
print_char 10 # 1238
ldint r96, 1 # 1239
addint r97, r93, r96 # 1240
pushint r97 # 1241
ldint r98, 10 # 1242
ltint r99, r97, r98 # 1243
jmpnz r99, -15 # 1244
reqbl 124 # 1245
reqbl 124 # 1246
