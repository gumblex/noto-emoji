#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import numpy as np
from skimage.color import rgb2lab, deltaE_ciede2000

COLORS_RGB = np.array(((
(255, 255, 255), #FFFFFF
(47, 47, 47), #2F2F2F
(68, 68, 68), #444444
(252, 194, 27), #FCC21B
(251, 193, 27), #FBC11B
(112, 83, 74), #70534A
(109, 76, 65), #6D4C41
(250, 220, 188), #FADCBC
(155, 100, 60), #9B643C
(191, 143, 104), #BF8F68
(224, 187, 149), #E0BB95
(35, 32, 32), #232020
(237, 108, 48), #ED6C30
(224, 224, 224), #E0E0E0
(122, 76, 50), #7A4C32
(153, 103, 79), #99674F
(219, 166, 137), #DBA689
(196, 142, 106), #C48E6A
(101, 31, 255), #651FFF
(120, 163, 173), #78A3AD
(86, 62, 55), #563E37
(69, 104, 173), #4568AD
(247, 147, 41), #F79329
(64, 192, 231), #40C0E7
(0, 220, 0), #00DC00
(38, 38, 38), #262626
(66, 49, 44), #42312C
(93, 64, 55), #5D4037
(133, 92, 82), #855C52
(117, 117, 117), #757575
(227, 158, 73), #E39E49
(41, 182, 246), #29B6F6
(100, 100, 100), #646464
(229, 150, 0), #E59600
(0, 191, 165), #00BFA5
(49, 45, 45), #312D2D
(71, 53, 45), #47352D
(191, 160, 85), #BFA055
(73, 54, 46), #49362E
(189, 189, 189), #BDBDBD
(228, 149, 0), #E49500
(81, 63, 53), #513F35
(0, 108, 162), #006CA2
(0, 190, 164), #00BEA4
(53, 32, 26), #35201A
(255, 193, 7), #FFC107
(249, 245, 237), #F9F5ED
(228, 140, 21), #E48C15
(110, 188, 197), #6EBCC5
(250, 192, 27), #FAC01B
(227, 148, 0), #E39400
(255, 179, 0), #FFB300
(69, 90, 100), #455A64
(189, 207, 70), #BDCF46
(215, 89, 139), #D7598B
(117, 127, 63), #757F3F
(193, 123, 71), #C17B47
(4, 162, 135), #04A287
(238, 238, 238), #EEEEEE
(144, 164, 174), #90A4AE
(229, 153, 0), #E59900
(112, 67, 36), #704324
(196, 198, 199), #C4C6C7
(33, 33, 33), #212121
(168, 168, 168), #A8A8A8
(2, 119, 189), #0277BD
(245, 245, 245), #F5F5F5
(54, 21, 175), #3615AF
(97, 97, 97), #616161
(250, 192, 54), #FAC036
(38, 198, 218), #26C6DA
(68, 170, 126), #44AA7E
(165, 88, 70), #A55846
(184, 146, 120), #B89278
(55, 71, 79), #37474F
(33, 30, 30), #211E1E
(110, 113, 119), #6E7177
(176, 190, 197), #B0BEC5
(255, 18, 0), #FF1200
(255, 109, 0), #FF6D00
(255, 255, 0), #FFFF00
(66, 66, 66), #424242
(129, 140, 155), #818C9B
(245, 124, 0), #F57C00
(76, 55, 52), #4C3734
(166, 169, 178), #A6A9B2
(89, 102, 124), #59667C
(221, 83, 34), #DD5322
(158, 158, 158), #9E9E9E
(230, 81, 0), #E65100
(0, 67, 115), #004373
(225, 245, 254), #E1F5FE
(255, 111, 0), #FF6F00
(149, 150, 153), #959699
(84, 110, 122), #546E7A
(251, 194, 26), #FBC21A
(244, 213, 152), #F4D598
(1, 87, 155), #01579B
(228, 152, 0), #E49800
(60, 43, 36), #3C2B24
(170, 0, 255), #AA00FF
(209, 196, 233), #D1C4E9
(229, 179, 90), #E5B35A
(236, 108, 48), #EC6C30
(253, 216, 53), #FDD835
(255, 235, 59), #FFEB3B
(59, 120, 231), #3B78E7
(229, 57, 53), #E53935
(255, 234, 0), #FFEA00
(38, 24, 25), #261819
(192, 123, 71), #C07B47
(219, 68, 55), #DB4437
(3, 155, 229), #039BE5
(35, 31, 32), #231F20
(86, 97, 114), #566172
(165, 169, 170), #A5A9AA
(170, 68, 68), #AA4444
(239, 83, 80), #EF5350
(41, 98, 255), #2962FF
(252, 212, 181), #FCD4B5
(51, 0, 0), #330000
(124, 179, 66), #7CB342
(128, 203, 196), #80CBC4
(120, 144, 156), #78909C
(21, 101, 192), #1565C0
(42, 86, 198), #2A56C6
(120, 162, 172), #78A2AC
(141, 110, 99), #8D6E63
(135, 90, 59), #875A3B
(1, 73, 122), #01497A
(63, 81, 181), #3F51B5
(124, 125, 125), #7C7D7D
(207, 216, 220), #CFD8DC
(209, 211, 212), #D1D3D4
(35, 24, 21), #231815
(167, 169, 172), #A7A9AC
(243, 188, 45), #F3BC2D
(255, 183, 77), #FFB74D
(38, 166, 154), #26A69A
(66, 65, 67), #424143
(88, 69, 57), #584539
(101, 30, 255), #651EFF
(179, 229, 252), #B3E5FC
(216, 216, 216), #D8D8D8
(255, 204, 0), #FFCC00
(188, 170, 164), #BCAAA4
(183, 145, 120), #B79178
(191, 54, 12), #BF360C
(193, 24, 16), #C11810
(221, 44, 0), #DD2C00
(249, 224, 115), #F9E073
(26, 108, 162), #1A6CA2
(25, 108, 162), #196CA2
(178, 24, 24), #B21818
(216, 96, 48), #D86030
(255, 193, 72), #FFC148
(229, 163, 21), #E5A315
(77, 81, 86), #4D5156
(0, 121, 107), #00796B
(161, 136, 127), #A1887F
(239, 108, 0), #EF6C00
(3, 58, 89), #033A59
(8, 156, 88), #089C58
(10, 10, 10), #0A0A0A
(40, 53, 147), #283593
(65, 64, 66), #414042
(84, 125, 190), #547DBE
(87, 87, 87), #575757
(100, 135, 142), #64878E
(180, 32, 2), #B42002
(183, 28, 28), #B71C1C
(198, 40, 40), #C62828
(219, 68, 54), #DB4436
(227, 242, 253), #E3F2FD
(245, 145, 41), #F59129
(246, 146, 41), #F69229
(251, 184, 23), #FBB817
(255, 87, 34), #FF5722
(255, 238, 88), #FFEE58
(244, 129, 32), #F48120
(247, 203, 77), #F7CB4D
(4, 132, 108), #04846C
(56, 144, 249), #3890F9
(178, 223, 219), #B2DFDB
(232, 162, 61), #E8A23D
(70, 70, 70), #464646
(118, 157, 167), #769DA7
(216, 190, 255), #D8BEFF
(0, 172, 193), #00ACC1
(133, 138, 147), #858A93
(149, 200, 236), #95C8EC
(0, 200, 83), #00C853
(5, 162, 135), #05A287
(32, 18, 132), #201284
(59, 196, 238), #3BC4EE
(127, 19, 1), #7F1301
(132, 132, 132), #848484
(142, 142, 142), #8E8E8E
(219, 94, 44), #DB5E2C
(234, 150, 15), #EA960F
(250, 250, 250), #FAFAFA
(255, 0, 0), #FF0000
(255, 61, 0), #FF3D00
(255, 110, 64), #FF6E40
(255, 145, 0), #FF9100
(255, 173, 26), #FFAD1A
(255, 196, 0), #FFC400
(255, 202, 40), #FFCA28
(255, 205, 62), #FFCD3E
(53, 38, 32), #352620
(121, 85, 72), #795548
(231, 86, 37), #E75625
(231, 161, 61), #E7A13D
(129, 212, 250), #81D4FA
(165, 171, 59), #A5AB3B
(204, 153, 102), #CC9966
(205, 203, 191), #CDCBBF
(236, 239, 241), #ECEFF1
(244, 67, 54), #F44336
(0, 108, 160), #006CA0
(204, 204, 204), #CCCCCC
(255, 167, 38), #FFA726
(33, 39, 43), #21272B
(38, 50, 56), #263238
(60, 71, 76), #3C474C
(66, 133, 244), #4285F4
(121, 165, 175), #79A5AF
(153, 153, 153), #999999
(196, 121, 48), #C47930
(243, 105, 59), #F3693B
(247, 146, 41), #F79229
(0, 118, 137), #007689
(8, 8, 8), #080808
(22, 167, 218), #16A7DA
(33, 150, 243), #2196F3
(112, 178, 226), #70B2E2
(125, 125, 125), #7D7D7D
(147, 147, 147), #939393
(230, 74, 25), #E64A19
(254, 246, 224), #FEF6E0
(13, 71, 161), #0D47A1
(77, 208, 225), #4DD0E1
(85, 139, 47), #558B2F
(96, 57, 19), #603913
(96, 125, 139), #607D8B
(98, 110, 48), #626E30
(117, 76, 41), #754C29
(122, 209, 252), #7AD1FC
(123, 31, 162), #7B1FA2
(129, 199, 132), #81C784
(139, 94, 60), #8B5E3C
(142, 36, 170), #8E24AA
(168, 0, 255), #A800FF
(171, 71, 188), #AB47BC
(174, 213, 129), #AED581
(183, 183, 183), #B7B7B7
(185, 205, 210), #B9CDD2
(187, 222, 251), #BBDEFB
(195, 13, 35), #C30D23
(204, 64, 121), #CC4079
(211, 209, 197), #D3D1C5
(228, 159, 73), #E49F49
(228, 163, 36), #E4A324
(229, 115, 115), #E57373
(242, 179, 27), #F2B31B
(244, 132, 32), #F48420
(245, 135, 32), #F58720
(245, 138, 31), #F58A1F
(246, 141, 31), #F68D1F
(246, 144, 31), #F6901F
(246, 148, 31), #F6941F
(247, 151, 30), #F7971E
(247, 154, 30), #F79A1E
(247, 157, 30), #F79D1E
(248, 160, 30), #F8A01E
(248, 163, 29), #F8A31D
(249, 166, 29), #F9A61D
(249, 169, 29), #F9A91D
(249, 172, 29), #F9AC1D
(250, 175, 28), #FAAF1C
(250, 179, 28), #FAB31C
(250, 182, 28), #FAB61C
(251, 185, 28), #FBB91C
(251, 188, 27), #FBBC1B
(252, 191, 27), #FCBF1B
(255, 124, 229), #FF7CE5
(102, 148, 158), #66949E
(160, 51, 2), #A03302
(227, 235, 238), #E3EBEE
(93, 165, 176), #5DA5B0
(175, 197, 204), #AFC5CC
(184, 233, 244), #B8E9F4
(227, 139, 21), #E38B15
(228, 231, 233), #E4E7E9
(230, 238, 239), #E6EEEF
(0, 87, 146), #005792
(101, 135, 141), #65878D
(104, 159, 56), #689F38
(204, 51, 51), #CC3333
(211, 211, 211), #D3D3D3
(217, 219, 221), #D9DBDD
(221, 87, 40), #DD5728
(233, 189, 170), #E9BDAA
(237, 236, 228), #EDECE4
(242, 192, 124), #F2C07C
(255, 143, 0), #FF8F00
(255, 204, 51), #FFCC33
(16, 107, 164), #106BA4
(68, 101, 104), #446568
(75, 101, 102), #4B6566
(77, 182, 172), #4DB6AC
(103, 122, 130), #677A82
(114, 73, 65), #724941
(114, 127, 72), #727F48
(136, 92, 82), #885C52
(147, 144, 144), #939090
(188, 210, 211), #BCD2D3
(205, 69, 37), #CD4525
(206, 69, 37), #CE4525
(226, 217, 195), #E2D9C3
(228, 151, 37), #E49725
(0, 229, 255), #00E5FF
(66, 99, 105), #426369
(89, 198, 217), #59C6D9
(149, 173, 50), #95AD32
(192, 202, 51), #C0CA33
(219, 221, 142), #DBDD8E
(226, 140, 37), #E28C25
(236, 175, 76), #ECAF4C
(243, 112, 33), #F37021
(244, 233, 176), #F4E9B0
(245, 146, 82), #F59252
(246, 236, 191), #F6ECBF
(247, 149, 40), #F79528
(247, 151, 40), #F79728
(248, 154, 39), #F89A27
(248, 156, 38), #F89C26
(248, 158, 38), #F89E26
(248, 160, 37), #F8A025
(249, 163, 36), #F9A324
(249, 165, 36), #F9A524
(249, 167, 35), #F9A723
(249, 169, 34), #F9A922
(250, 172, 34), #FAAC22
(250, 174, 33), #FAAE21
(250, 176, 32), #FAB020
(250, 178, 32), #FAB220
(250, 218, 128), #FADA80
(251, 181, 31), #FBB51F
(251, 183, 30), #FBB71E
(251, 185, 30), #FBB91E
(251, 187, 29), #FBBB1D
(252, 190, 28), #FCBE1C
(252, 192, 28), #FCC01C
(0, 230, 118), #00E676
(1, 108, 162), #016CA2
(1, 190, 164), #01BEA4
(6, 109, 163), #066DA3
(46, 125, 50), #2E7D32
(102, 51, 51), #663333
(117, 117, 118), #757576
(134, 92, 81), #865C51
(137, 137, 137), #898989
(139, 89, 64), #8B5940
(155, 137, 132), #9B8984
(166, 111, 0), #A66F00
(173, 35, 21), #AD2315
(178, 178, 179), #B2B2B3
(181, 23, 15), #B5170F
(181, 225, 234), #B5E1EA
(186, 186, 186), #BABABA
(188, 190, 192), #BCBEC0
(188, 206, 70), #BCCE46
(190, 32, 6), #BE2006
(194, 194, 194), #C2C2C2
(204, 232, 255), #CCE8FF
(209, 235, 237), #D1EBED
(210, 221, 225), #D2DDE1
(213, 0, 249), #D500F9
(216, 27, 96), #D81B60
(216, 67, 21), #D84315
(221, 23, 14), #DD170E
(225, 190, 231), #E1BEE7
(226, 234, 237), #E2EAED
(228, 227, 222), #E4E3DE
(236, 64, 122), #EC407A
(237, 28, 36), #ED1C24
(239, 65, 54), #EF4136
(240, 98, 146), #F06292
(241, 90, 41), #F15A29
(248, 190, 54), #F8BE36
(255, 80, 80), #FF5050
(25, 92, 130), #195C82
(51, 51, 51), #333333
(55, 180, 226), #37B4E2
(70, 71, 71), #464747
(102, 72, 66), #664842
(104, 145, 154), #68919A
(136, 14, 79), #880E4F
(140, 213, 245), #8CD5F5
(173, 20, 87), #AD1457
(173, 138, 115), #AD8A73
(191, 133, 4), #BF8504
(193, 174, 170), #C1AEAA
(206, 69, 62), #CE453E
(224, 96, 85), #E06055
(229, 80, 46), #E5502E
(229, 171, 76), #E5AB4C
(238, 186, 115), #EEBA73
(250, 193, 28), #FAC11C
(250, 194, 28), #FAC21C
(251, 192, 27), #FBC01B
(251, 204, 47), #FBCC2F
(252, 232, 178), #FCE8B2
(254, 144, 64), #FE9040
(255, 220, 174), #FFDCAE
(30, 136, 229), #1E88E5
(47, 47, 47), #2f2f2f
(47, 48, 47), #2F302F
(61, 136, 195), #3D88C3
(81, 49, 24), #513118
(93, 65, 55), #5D4137
(102, 103, 102), #666766
(135, 94, 84), #875E54
(153, 169, 90), #99A95A
(154, 170, 95), #9AAA5F
(157, 105, 172), #9D69AC
(174, 61, 9), #AE3D09
(174, 206, 206), #AECECE
(177, 224, 207), #B1E0CF
(180, 233, 243), #B4E9F3
(226, 195, 64), #E2C340
(227, 173, 80), #E3AD50
(229, 130, 59), #E5823B
(229, 167, 12), #E5A70C
(236, 34, 20), #EC2214
(236, 108, 47), #EC6C2F
(237, 128, 173), #ED80AD
(244, 134, 92), #F4865C
(245, 211, 133), #F5D385
(249, 192, 53), #F9C035
(252, 135, 89), #FC8759
(255, 211, 147), #FFD393
(0, 51, 102), #003366
(0, 77, 64), #004D40
(0, 131, 143), #00838F
(2, 136, 209), #0288D1
(3, 169, 244), #03A9F4
(43, 56, 17), #2B3811
(66, 192, 231), #42C0E7
(69, 39, 160), #4527A0
(71, 76, 79), #474C4F
(79, 47, 39), #4F2F27
(104, 69, 45), #68452D
(109, 139, 20), #6D8B14
(110, 140, 22), #6E8C16
(119, 66, 204), #7742CC
(119, 163, 174), #77A3AE
(120, 161, 171), #78A1AB
(128, 60, 61), #803C3D
(129, 176, 18), #81B012
(133, 87, 49), #855731
(138, 177, 183), #8AB1B7
(139, 172, 178), #8BACB2
(175, 131, 102), #AF8366
(175, 235, 243), #AFEBF3
(176, 181, 114), #B0B572
(181, 195, 198), #B5C3C6
(185, 50, 33), #B93221
(185, 89, 48), #B95930
(185, 232, 244), #B9E8F4
(188, 205, 70), #BCCD46
(190, 25, 49), #BE1931
(198, 55, 32), #C63720
(206, 206, 210), #CECED2
(218, 67, 61), #DA433D
(220, 46, 7), #DC2E07
(223, 231, 234), #DFE7EA
(224, 222, 213), #E0DED5
(225, 81, 72), #E15148
(226, 138, 21), #E28A15
(226, 210, 186), #E2D2BA
(229, 137, 47), #E5892F
(233, 226, 207), #E9E2CF
(234, 72, 50), #EA4832
(234, 234, 234), #EAEAEA
(237, 175, 77), #EDAF4D
(242, 186, 148), #F2BA94
(246, 228, 153), #F6E499
(246, 246, 246), #F6F6F6
(247, 182, 24), #F7B618
(249, 227, 212), #F9E3D4
(249, 244, 217), #F9F4D9
(250, 193, 29), #FAC11D
(253, 215, 119), #FDD777
(255, 204, 128), #FFCC80
(255, 224, 178), #FFE0B2
(255, 241, 212), #FFF1D4
(255, 243, 171), #FFF3AB
(0, 137, 123), #00897B
(1, 109, 158), #016D9E
(3, 69, 114), #034572
(7, 104, 148), #076894
(15, 109, 160), #0F6DA0
(38, 168, 198), #26A8C6
(43, 139, 193), #2B8BC1
(44, 182, 211), #2CB6D3
(46, 47, 47), #2E2F2F
(55, 101, 75), #37654B
(59, 43, 35), #3B2B23
(59, 178, 222), #3BB2DE
(59, 178, 223), #3BB2DF
(63, 63, 63), #3F3F3F
(63, 191, 231), #3FBFE7
(64, 55, 50), #403732
(69, 67, 63), #45433F
(69, 76, 41), #454C29
(72, 192, 229), #48C0E5
(73, 51, 48), #493330
(75, 167, 188), #4BA7BC
(76, 175, 80), #4CAF50
(86, 170, 236), #56AAEC
(99, 135, 143), #63878F
(100, 181, 246), #64B5F6
(103, 147, 156), #67939C
(110, 69, 29), #6E451D
(112, 157, 166), #709DA6
(117, 104, 94), #75685E
(121, 163, 172), #79A3AC
(130, 87, 81), #825751
(134, 90, 61), #865A3D
(134, 163, 44), #86A32C
(134, 212, 238), #86D4EE
(137, 91, 83), #895B53
(152, 170, 48), #98AA30
(153, 16, 82), #991052
(155, 16, 83), #9B1053
(159, 54, 33), #9F3621
(167, 48, 15), #A7300F
(170, 118, 115), #AA7673
(173, 173, 173), #ADADAD
(174, 210, 211), #AED2D3
(178, 235, 242), #B2EBF2
(179, 56, 106), #B3386A
(183, 146, 120), #B79278
(183, 159, 152), #B79F98
(187, 145, 122), #BB917A
(193, 144, 72), #C19048
(194, 24, 91), #C2185B
(196, 166, 106), #C4A66A
(198, 159, 133), #C69F85
(198, 198, 198), #C6C6C6
(199, 227, 229), #C7E3E5
(203, 146, 101), #CB9265
(204, 123, 50), #CC7B32
(206, 90, 44), #CE5A2C
(206, 207, 209), #CECFD1
(209, 193, 189), #D1C1BD
(214, 172, 144), #D6AC90
(218, 68, 55), #DA4437
(221, 164, 80), #DDA450
(222, 221, 221), #DEDDDD
(225, 225, 225), #E1E1E1
(227, 151, 0), #E39700
(228, 63, 17), #E43F11
(232, 159, 15), #E89F0F
(233, 184, 119), #E9B877
(234, 89, 110), #EA596E
(235, 128, 171), #EB80AB
(239, 235, 233), #EFEBE9
(241, 187, 38), #F1BB26
(247, 201, 119), #F7C977
(247, 239, 218), #F7EFDA
(249, 163, 113), #F9A371
(249, 167, 21), #F9A715
(249, 183, 25), #F9B719
(249, 210, 142), #F9D28E
(250, 193, 54), #FAC136
(252, 208, 167), #FCD0A7
(252, 219, 179), #FCDBB3
(252, 223, 181), #FCDFB5
(252, 228, 184), #FCE4B8
(252, 232, 187), #FCE8BB
(253, 187, 159), #FDBB9F
(253, 192, 162), #FDC0A2
(253, 196, 165), #FDC4A5
(253, 201, 167), #FDC9A7
(253, 205, 170), #FDCDAA
(253, 210, 173), #FDD2AD
(253, 214, 176), #FDD6B0
(254, 156, 139), #FE9C8B
(254, 160, 142), #FEA08E
(254, 165, 145), #FEA591
(254, 169, 148), #FEA994
(254, 174, 150), #FEAE96
(254, 178, 153), #FEB299
(254, 183, 156), #FEB79C
(255, 138, 128), #FF8A80
(255, 142, 131), #FF8E83
(255, 147, 134), #FF9386
(255, 151, 136), #FF9788
(255, 152, 0), #FF9800
(255, 224, 130), #FFE082
(255, 242, 211), #FFF2D3
(255, 243, 224), #FFF3E0
(255, 244, 203), #FFF4CB
(0, 107, 167), #006BA7
(0, 175, 236), #00AFEC
(0, 188, 213), #00BCD5
(0, 191, 239), #00BFEF
(6, 150, 166), #0696A6
(10, 79, 109), #0A4F6D
(15, 157, 88), #0F9D58
(20, 19, 19), #141313
(25, 67, 45), #19432D
(25, 105, 157), #19699D
(30, 132, 188), #1E84BC
(31, 31, 31), #1F1F1F
(40, 113, 163), #2871A3
(41, 35, 35), #292323
(41, 79, 110), #294F6E
(43, 148, 197), #2B94C5
(47, 32, 27), #2F201B
(49, 55, 56), #313738
(55, 191, 233), #37BFE9
(57, 91, 43), #395B2B
(58, 58, 58), #3A3A3A
(65, 132, 175), #4184AF
(66, 21, 3), #421503
(69, 74, 76), #454A4C
(70, 104, 30), #46681E
(71, 71, 71), #474747
(71, 192, 229), #47C0E5
(74, 53, 48), #4A3530
(78, 52, 46), #4E342E
(78, 195, 228), #4EC3E4
(79, 79, 79), #4F4F4F
(80, 123, 130), #507B82
(84, 102, 112), #546670
(84, 149, 178), #5495B2
(85, 120, 124), #55787C
(85, 167, 208), #55A7D0
(89, 52, 45), #59342D
(91, 66, 58), #5B423A
(92, 133, 135), #5C8587
(93, 93, 93), #5D5D5D
(94, 56, 50), #5E3832
(96, 55, 26), #60371A
(100, 117, 139), #64758B
(106, 57, 6), #6A3906
(107, 144, 150), #6B9096
(108, 72, 40), #6C4828
(109, 114, 42), #6D722A
(110, 110, 110), #6E6E6E
(113, 73, 66), #714942
(113, 211, 234), #71D3EA
(114, 8, 69), #720845
(119, 162, 173), #77A2AD
(119, 163, 173), #77A3AD
(119, 185, 79), #77B94F
(121, 162, 172), #79A2AC
(124, 94, 84), #7C5E54
(134, 93, 83), #865D53
(136, 90, 56), #885A38
(137, 192, 229), #89C0E5
(138, 181, 188), #8AB5BC
(140, 234, 231), #8CEAE7
(144, 68, 39), #904427
(144, 110, 65), #906E41
(145, 117, 97), #917561
(147, 191, 198), #93BFC6
(152, 152, 152), #989898
(153, 89, 32), #995920
(155, 122, 38), #9B7A26
(156, 156, 159), #9C9C9F
(159, 186, 86), #9FBA56
(160, 182, 50), #A0B632
(160, 186, 123), #A0BA7B
(161, 51, 0), #A13300
(162, 192, 43), #A2C02B
(163, 163, 13), #A3A30D
(164, 181, 190), #A4B5BE
(165, 39, 20), #A52714
(165, 194, 17), #A5C211
(165, 194, 19), #A5C213
(167, 82, 19), #A75213
(168, 98, 41), #A86229
(168, 222, 234), #A8DEEA
(169, 183, 191), #A9B7BF
(170, 129, 101), #AA8165
(170, 234, 249), #AAEAF9
(175, 85, 49), #AF5531
(175, 180, 43), #AFB42B
(177, 201, 55), #B1C937
(178, 178, 178), #B2B2B2
(179, 191, 66), #B3BF42
(179, 244, 229), #B3F4E5
(180, 199, 204), #B4C7CC
(180, 210, 28), #B4D21C
(181, 210, 28), #B5D21C
(183, 136, 90), #B7885A
(184, 145, 120), #B89178
(185, 145, 118), #B99176
(185, 146, 118), #B99276
(186, 148, 122), #BA947A
(186, 233, 243), #BAE9F3
(188, 207, 56), #BCCF38
(189, 170, 164), #BDAAA4
(190, 232, 241), #BEE8F1
(193, 191, 180), #C1BFB4
(194, 175, 168), #C2AFA8
(194, 203, 206), #C2CBCE
(195, 129, 48), #C38130
(197, 197, 197), #C5C5C5
(197, 225, 165), #C5E1A5
(199, 228, 234), #C7E4EA
(201, 191, 147), #C9BF93
(201, 205, 205), #C9CDCD
(203, 213, 220), #CBD5DC
(204, 77, 33), #CC4D21
(204, 182, 86), #CCB656
(204, 192, 143), #CCC08F
(204, 203, 203), #CCCBCB
(205, 128, 31), #CD801F
(206, 91, 43), #CE5B2B
(206, 207, 208), #CECFD0
(207, 208, 209), #CFD0D1
(208, 228, 104), #D0E468
(209, 155, 21), #D19B15
(211, 161, 102), #D3A166
(211, 203, 167), #D3CBA7
(211, 208, 196), #D3D0C4
(211, 222, 226), #D3DEE2
(212, 236, 244), #D4ECF4
(214, 69, 69), #D64545
(214, 90, 140), #D65A8C
(214, 91, 41), #D65B29
(215, 204, 200), #D7CCC8
(216, 91, 42), #D85B2A
(216, 125, 43), #D87D2B
(216, 204, 200), #D8CCC8
(216, 206, 164), #D8CEA4
(220, 127, 39), #DC7F27
(221, 131, 215), #DD83D7
(221, 214, 191), #DDD6BF
(222, 83, 35), #DE5323
(223, 76, 73), #DF4C49
(224, 247, 250), #E0F7FA
(225, 232, 237), #E1E8ED
(226, 214, 179), #E2D6B3
(228, 167, 36), #E4A724
(229, 208, 122), #E5D07A
(229, 221, 160), #E5DDA0
(229, 229, 229), #E5E5E5
(230, 231, 232), #E6E7E8
(230, 238, 156), #E6EE9C
(232, 210, 116), #E8D274
(232, 225, 193), #E8E1C1
(232, 226, 217), #E8E2D9
(233, 95, 93), #E95F5D
(234, 108, 58), #EA6C3A
(234, 109, 71), #EA6D47
(234, 136, 169), #EA88A9
(234, 169, 232), #EAA9E8
(234, 227, 197), #EAE3C5
(235, 107, 48), #EB6B30
(235, 168, 27), #EBA81B
(235, 234, 226), #EBEAE2
(235, 241, 242), #EBF1F2
(237, 108, 48), #ed6c30
(237, 109, 49), #ED6D31
(237, 162, 155), #EDA29B
(237, 176, 78), #EDB04E
(239, 107, 0), #EF6B00
(239, 119, 72), #EF7748
(239, 157, 1), #EF9D01
(239, 183, 142), #EFB78E
(239, 199, 127), #EFC77F
(240, 147, 0), #F09300
(241, 89, 43), #F1592B
(241, 248, 233), #F1F8E9
(242, 67, 56), #F24338
(242, 102, 96), #F26660
(242, 241, 235), #F2F1EB
(244, 130, 99), #F48263
(244, 138, 132), #F48A84
(244, 237, 211), #F4EDD3
(244, 239, 228), #F4EFE4
(245, 234, 150), #F5EA96
(246, 229, 153), #F6E599
(246, 238, 218), #F6EEDA
(247, 147, 42), #F7932A
(247, 229, 153), #F7E599
(248, 142, 0), #F88E00
(248, 182, 24), #F8B618
(248, 216, 192), #F8D8C0
(248, 225, 170), #F8E1AA
(249, 174, 75), #F9AE4B
(250, 204, 48), #FACC30
(250, 215, 141), #FAD78D
(252, 194, 26), #FCC21A
(252, 194, 27), #fcc21b
(252, 194, 28), #FCC21C
(252, 195, 27), #FCC31B
(252, 212, 182), #FCD4B6
(253, 203, 128), #FDCB80
(253, 216, 54), #FDD836
(253, 226, 131), #FDE283
(254, 243, 205), #FEF3CD
(255, 112, 67), #FF7043
(255, 171, 0), #FFAB00
(255, 171, 145), #FFAB91
(255, 191, 36), #FFBF24
(255, 203, 40), #FFCB28
(255, 204, 188), #FFCCBC
(255, 205, 80), #FFCD50
(255, 208, 95), #FFD05F
(255, 213, 79), #FFD54F
(255, 226, 102), #FFE266
(255, 229, 127), #FFE57F
(255, 230, 179), #FFE6B3
(255, 238, 204), #FFEECC
(255, 242, 212), #FFF2D4
(255, 243, 202), #FFF3CA
(255, 246, 159), #FFF69F
(255, 249, 215), #FFF9D7
),))

COLORS_LAB = rgb2lab(COLORS_RGB / 255.0)

while 1:
    try:
        clr = input('> ')
    except EOFError:
        break
    clr = clr.lstrip('#')
    vec = np.array((((int(clr[:2], 16), int(clr[2:4], 16), int(clr[4:6], 16)),),))
    vec_lab = rgb2lab(vec / 255.0)[0][0]
    dist = deltaE_ciede2000(COLORS_LAB, vec_lab)
    minclr = np.argmin(dist[0])
    print('%02x%02x%02x' % tuple(COLORS_RGB[0][minclr]))
