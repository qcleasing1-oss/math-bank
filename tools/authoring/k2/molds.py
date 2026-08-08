# -*- coding: utf-8 -*-
"""ทะเบียนแม่พิมพ์ (mold registry) · ด่าน STEP H รุ่นที่ 4

═══ ทำไมต้องเลิกใช้ตัวจับความคล้ายของถ้อยคำ ═══
nearcheck v1/v2/v3 ล้มทั้งสามรุ่น เหตุผลไม่ใช่จูนพารามิเตอร์ไม่ดี แต่เป็นเหตุผลเชิงโครงสร้าง
ข้อสอบไทยใช้สำนวนมาตรฐานร่วมกันเกือบทุกข้อ ("กำหนดให้ ... เป็นจำนวนจริงซึ่ง ...
ค่าของ ... เท่ากับข้อใดต่อไปนี้") ⇒ ตัววัดความคล้ายของถ้อยคำวัด "สำนวน" ไม่ได้วัด "คณิตศาสตร์"
และคณิตศาสตร์คือสิ่งที่ตัว normalizer โยนทิ้งพอดี (ทิ้งตัวเลข ทิ้ง LaTeX)

ตัวเลขยืนยันหลังจากลบถ้อยคำสำเร็จรูปทิ้งแล้ว (v3):
    q025 ↔ q040(เก่า)  ซ้ำจริง        jac 0.34 · con 0.53
    q004 ↔ q022        คนละเรื่องเลย   jac 0.61 · con 0.81   ← สูงกว่าคู่ที่ซ้ำจริง
⇒ ตัววัดกลับหัว ใช้เป็นด่านไม่ได้ ไม่ว่าจะตั้งเกณฑ์ที่เท่าไร

═══ สิ่งที่ใช้แทน ═══
บันทึก "สามส่วนของแม่พิมพ์" ของทุกข้อด้วยมือ แล้วเทียบสามส่วนต่อสามส่วน
    G (โจทย์ให้อะไร) · A (ถามหาอะไร) · M (ใช้เครื่องมืออะไรแก้)
เกณฑ์:
    ❌ ตก      ตรงกันทั้งสามส่วน            = แม่พิมพ์เดียวกัน ผิดกฎเหล็กข้อ 5
    ⚠️ เฝ้าดู  M ตรง และ (G หรือ A) ตรง     = ทับกันสองส่วน ต้องตรวจด้วยตา
    ⚠️ เฝ้าดู  G และ A ตรง แต่ M ต่าง        = พื้นผิวเหมือน แต่คณิตศาสตร์คนละตัว มักผ่าน
    ✅ ผ่าน    นอกนั้น

⭐ วิธีใช้: ก่อนแต่งข้อใหม่ ให้เพิ่มบรรทัดของข้อนั้นลง PLAN แล้วรันไฟล์นี้
   ถ้าขึ้น ❌ ⇒ ห้ามแต่ง ต้องเปลี่ยนแม่พิมพ์ก่อน

═══ 🆕 8 ส.ค. 2569 · 3 ชั้นที่ทำให้ "กวาดคลังจริง" ขาดไม่ได้เชิงโครงสร้าง ═══
(ข้อเสนอ E→MB #43 §2 · ครูอนุมัติ "ทำครบ 3 ชั้น" 8 ส.ค. 69)

รากของอุบัติเหตุก้อน 22 ⛔ ไม่ใช่ "ลืมกวาด" — เป็น **ตัวหารผิด** :
    ไฟล์นี้ตอบคำถาม "ซ้ำของเราเองไหม" ได้ถูก 100% จาก 164 ข้อ
    แต่คนอ่านคิดว่ามันตอบ "เคยมีคนถามแล้วหรือยัง" ซึ่งตัวหารคือ 6,477 ข้อ
    ⇒ q165 (ชน samn-2559-12-q03) และ q174 (ชน alvl1-2566-03-q07) ผ่านด่านนี้แบบเขียว

ชั้น 1 · ตัวหารของด่าน = ตัวหารของคำถาม
    ไฟล์นี้ **นำเข้า bankscope** และอ่านคลังทั้งใบก่อนตัดสินทุกครั้ง
    อ่านคลังไม่ได้ ⇒ รหัสออก 2 (ตัวตรวจใช้ไม่ได้) ⛔ ไม่ใช่ "ผ่านเพราะไม่เจออะไร"
    ⇒ "ลงทะเบียนโดยยังไม่เคยเห็นคลังจริง" เกิดไม่ได้ — ไม่ใช่เพราะมีคนจำได้

ชั้น 2 · ป้ายตัวหารบังคับ (㊳ ขาที่ห้า ที่เขียนลงไฟล์ ⛔ ไม่ใช่เขียนลงจดหมาย)
    ทุกใบเสร็จพก `scope` = ป้ายของคลัง ณ วันกวาด (ไฟล์·ข้อ·ลายนิ้วมือ)
    ป้าย ≠ คลังวันนี้ ⇒ ❌ ใบเสร็จหมดอายุ ⇒ ต้องกวาดใหม่
    ⚠️ ลายนิ้วมืออยู่ในป้ายด้วยโดยตั้งใจ: ถอน 1 เพิ่ม 1 ⇒ ยอดนิ่ง แต่ของที่ต้องกวาดเปลี่ยนแล้ว

ชั้น 3 · ใบเสร็จบังคับ
    id ใน PLAN และ id ที่ลงทะเบียนใหม่ใน REG **ต้องมีใบเสร็จ** ไม่งั้น ❌
    ⚠️ 164 แถวเดิม (q001–q164) ลงทะเบียนก่อนกฎนี้มีอยู่ ⇒ อยู่ในรายการยกเว้น
       `PRE_RECEIPT` ซึ่งเป็น **กงล้อ: ลดได้อย่างเดียว** ⛔ ห้ามเติมชื่อเข้าไป
"""
import os
import sys

# ── ชั้น 1 · ตัวหารกลาง — ต้องนำเข้าได้ ไม่งั้นไฟล์นี้ตัดสินอะไรไม่ได้
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bankscope                                                   # noqa: E402

# ═══════════════════════ ทะเบียน 44 ข้อที่แต่งแล้ว ═══════════════════════
# (G โจทย์ให้, A ถามหา, M เครื่องมือหลัก)
REG = {
    'q001': ('G-TRI-ANY-TANRATIO',      'A-EXPR-VALUE',     'M-TAN-TRI-IDENT'),
    'q002': ('G-RATIO-EQ',              'A-SUM-PARAM',      'M-HALF-YUB'),
    'q003': ('G-REALWORLD-VIEWANGLE',   'A-EXTREME-ARG',    'M-AMGM'),
    'q004': ('G-RATIO-EQ',              'A-EXPR-VALUE',     'M-CUBE-FACTOR'),
    'q005': ('G-EQ-PARAM-INT',          'A-SUM-PARAM',      'M-PARAM-RANGE'),
    'q006': ('G-TRI-ANY-SIDESEQ-ANGREL', 'A-RATIO-VALUE',   'M-LAW-COS'),
    'q007': ('G-TRI-RT-IDENTEQ',        'A-RATIO-VALUE',    'M-PYTHID-CONJ'),
    'q008': ('G-UC-POINT',              'A-POINT',          'M-UC-SYMMETRY'),
    'q009': ('G-FUNC-UNKNOWN-PARAM',    'A-EXPR-VALUE',     'M-AMP-MID-PERIOD'),
    'q010': ('G-TRI-RT-2SIDE',          'A-RATIO-VALUE',    'M-PYTHAG-DEF'),
    'q011': ('G-ANGLE-ACUTE-RATIO',     'A-EXPR-VALUE',     'M-REF-TRIANGLE'),
    'q012': ('G-ANG-NUMERIC',           'A-EXPR-VALUE',     'M-REF-ANGLE-SIGN'),
    'q013': ('G-FUNC-FORM',             'A-EXTREME',        'M-RANGE-BOUND'),
    'q014': ('G-RATIO-EQ',              'A-EXPR-VALUE',     'M-PYTHID-EXPAND'),
    'q015': ('G-TRI-RT-1SIDE-RATIO',    'A-SIDE-LEN',       'M-PYTHAG-DEF'),
    'q016': ('G-ANG-NUMERIC',           'A-EXPR-VALUE',     'M-SUMDIFF'),
    'q017': ('G-ANGLE-ACUTE-RATIO',     'A-RATIO-VALUE',    'M-DOUBLE'),
    'q018': ('G-EQ-BASIC',              'A-ANGLE-VALUE',    'M-REF-ANGLE-SIGN'),
    'q019': ('G-TRI-ANY-2ANG-1SIDE',    'A-SIDE-LEN',       'M-LAW-SIN'),
    'q020': ('G-ANG-OVERTURN',          'A-RATIO-VALUE',    'M-MOD2PI'),
    'q021': ('G-UC-POINT',              'A-EXPR-VALUE',     'M-REDUCTION'),
    'q022': ('G-RATIO-SIGN',            'A-EXPR-VALUE',     'M-REF-TRIANGLE'),
    'q023': ('G-UC-QUAD-DIST',          'A-ANGLE-VALUE',    'M-DIST-FORMULA'),
    'q024': ('G-UC-REFLECT',            'A-SUM-ROOTS',      'M-SOLVE-SET-GENERAL'),
    'q025': ('G-FUNC-FORM',             'A-PERIOD',         'M-LCM-PERIOD'),
    'q026': ('G-GRAPH-TRANSFORM',       'A-EQUATION',       'M-TRANSFORM-ORDER'),
    'q027': ('G-GRAPH-SHIFT-MATCH',     'A-EXTREME-ARG',    'M-REDUCTION'),
    'q028': ('G-FUNC-FORM',             'A-DOMAIN-MEASURE', 'M-SOLVE-SET-GENERAL'),
    'q029': ('G-FUNC-FORM',             'A-EXTREME',        'M-ABS-PIECEWISE'),
    'q030': ('G-SECTOR-R-ANG',          'A-AREA',           'M-SECTOR-FORMULAS'),
    'q031': ('G-SECTOR-R-AREA',         'A-PERIMETER',      'M-SECTOR-FORMULAS'),
    'q032': ('G-SECTOR-CONCENTRIC',     'A-ARC-LEN',        'M-SECTOR-FORMULAS'),
    'q033': ('G-REALWORLD-PENDULUM',    'A-ARC-LEN',        'M-SECTOR-FORMULAS'),
    'q034': ('G-SECTOR-PERI-AREA',      'A-SUM-PARAM',      'M-SECTOR-FORMULAS'),
    'q035': ('G-UC-LINE-QUAD',          'A-EXPR-VALUE',     'M-LINE-INTERSECT-UC'),
    'q036': ('G-EXPR-RELANGLE',         'A-EXPR-VALUE',     'M-REDUCTION'),
    'q037': ('G-UC-PARAM-N',            'A-COUNT',          'M-COUNT-CYCLE'),
    'q038': ('G-FUNC-FORM',             'A-EXTREME',        'M-RANGE-RECIP'),
    'q039': ('G-TWO-GRAPHS',            'A-SUM-ROOTS',      'M-DOUBLE'),
    'q040': ('G-FUNC-FORM',             'A-UNDEFINED-ARG',  'M-DENOM-ZERO'),
    'q041': ('G-UC-ARCLEN-BIG',         'A-QUADRANT',       'M-MOD2PI'),
    'q042': ('G-RATIO-EQ',              'A-RATIO-VALUE',    'M-AUX-ANGLE'),
    'q043': ('G-TWO-GRAPHS',            'A-COUNT',          'M-GRAPH-COUNT'),
    'q044': ('G-FUNC-FORM',             'A-EXTREME',        'M-QUAD-IN-TRIG'),
    # ── ก้อน 8 · ย้ายจาก PLAN เข้าทะเบียนจริง หลังไฟล์ JSON ออกและผ่านสามด่านแล้ว ──
    'q045': ('G-SIGN-CONDITIONS',       'A-QUADRANT',          'M-SIGN-TABLE'),
    'q046': ('G-ANG-NUMERIC',           'A-ORDER',             'M-UC-COMPARE'),
    'q047': ('G-REALWORLD-SINUSOID',    'A-TIME-DURATION',     'M-INEQ-UC'),
    'q048': ('G-FUNC-FORM',             'A-INTERVAL-MONOTONE', 'M-MONOTONE-UC'),
    'q049': ('G-GRAPH-ZERO-COUNT',      'A-EXPR-VALUE',        'M-ZERO-COUNT-PARAM'),
    # ── ก้อน 9 · ย้ายจาก PLAN เข้าทะเบียนจริง หลังไฟล์ JSON ออกและผ่านสามด่านแล้ว ──
    'q050': ('G-ARC-EXPR-FORM',         'A-EXTREME-SPREAD',    'M-ARC-COMPLEMENT-QUAD'),
    'q051': ('G-ARC-EXPR-NUMERIC',      'A-ORDER',             'M-ARC-PRINCIPAL-FOLD'),
    'q052': ('G-ARC-COMPOSITE-QUAD',    'A-DOMAIN',            'M-DOUBLE-INEQ-QUAD'),
    'q053': ('G-TRI-SSA-PARAM',         'A-SUM-PARAM',         'M-AMBIGUOUS-EXISTENCE'),
    'q054': ('G-QUAD-4SIDE-OPPSUM',     'A-AREA',              'M-DIAG-TWICE-LAWCOS'),
    # ── ก้อน 10 · ย้ายจาก PLAN เข้าทะเบียนจริง หลังไฟล์ JSON ออกและผ่านสามด่านแล้ว ──
    # ⚠️ แก้ป้าย A ของ q056 ตอนย้าย : ตอนวางแผนจดไว้เป็น 'A-RATIO-VALUE' ซึ่งเป็นป้ายของ
    #    ฉบับก่อนกลับทิศ · ข้อที่แต่งจริงถาม cos ของมุมเต็ม ⇒ ป้ายที่ตรงของจริงคือ
    #    'A-FULLANGLE-COS' · การแก้นี้ทำให้ข้อ "ต่างจากของเดิมมากขึ้น" ไม่ใช่ซ่อนการชน
    #    (รันเทียบทั้งสองป้ายแล้ว ❌ = 0 คู่ และไม่มีคู่ WATCH ใหม่ทั้งสองแบบ)
    'q055': ('G-IDENTITY-COEFF-FORM',   'A-COEFF-RATIO',       'M-POWER-REDUCTION'),
    'q056': ('G-HALFANGLE-EXPR-VALUE',  'A-FULLANGLE-COS',     'M-HALFANGLE-COLLAPSE'),
    'q057': ('G-EQ-EQUAL-SINE',         'A-COUNT-SOLUTIONS',   'M-TWO-BRANCH-DEDUP'),
    'q058': ('G-SUMDIFF-PAIR-VALUES',   'A-TAN-RATIO',         'M-SPLIT-SUMDIFF'),
    'q059': ('G-PARAM-EQ-COS2X-PLUS-COSX', 'A-PARAM-SET',      'M-DOUBLE-ANGLE-FACTOR-EXACT-COUNT'),
    # ── ก้อน 11 · ย้ายจาก PLAN เข้าทะเบียนจริง หลังไฟล์ JSON ออกและผ่านสามด่านแล้ว ──
    #    (check_k2 0 จุด · ด่าน 7 หนี้ใหม่ 0 ข้อ · audit44 สะสม 64 ข้อ 0 ปัญหา)
    #    ป้ายทั้งห้าแถวย้ายมาตรงตัว ไม่มีการแก้ป้ายระหว่างย้ายในก้อนนี้
    'q060': ('G-SECTOR-R-ARC',          'A-ANGLE-DEGREE',      'M-ARC-RAD-TO-DEG'),
    'q061': ('G-TRI-SAS-OBTUSE',        'A-AREA',              'M-AREA-HALF-AB-SIN'),
    'q062': ('G-ANG-RADIAN-NEG-BIG',    'A-COTERMINAL-ANGLE',  'M-COTERMINAL-REDUCE'),
    'q063': ('G-TRI-IDENT-CONDITION',   'A-TRIANGLE-TYPE',     'M-LAWSIN-DOUBLE-TWO-BRANCH'),
    'q064': ('G-TRI-SIDES-AP-INTEGER',  'A-COUNT-PARAM',       'M-OBTUSE-CRITERION-PLUS-INEQ'),
    # ── ก้อน 12 · ย้ายจาก PLAN เข้าทะเบียนจริง หลังไฟล์ JSON ออกและผ่านสามด่านแล้ว ──
    #    (check_k2 0 จุด · ด่าน 7 หนี้ใหม่ 0 ข้อ · audit44 สะสม 69 ข้อ 0 ปัญหา)
    #    ป้ายทั้งห้าแถวย้ายมาตรงตัว ไม่มีการแก้ป้ายระหว่างย้ายในก้อนนี้
    'q065': ('G-RIGHT-TRI-TWO-LEGS',    'A-COMPOSITE-RATIO-EXPR', 'M-PYTHAGORAS-THEN-COMPOSE'),
    'q066': ('G-TWO-PULLEYS-BELT',      'A-ANGULAR-SPEED-RPM',    'M-EQUAL-LINEAR-SPEED-R-OMEGA'),
    'q067': ('G-ARCCOS-LINEAR-ARG',     'A-COUNT-INTEGERS',       'M-DOMAIN-INEQUALITY-COUNT'),
    'q068': ('G-EARTH-LATITUDE-CIRCLE', 'A-DIST-ALONG-PARALLEL',  'M-SMALL-CIRCLE-RADIUS-THEN-ARC'),
    'q069': ('G-TRI-SIDE-AND-OPP-ANGLE', 'A-PERIMETER-RANGE',     'M-LAWSIN-SUM-TO-PRODUCT-ENDPOINTS'),
    # ── ก้อน 13 · ย้ายจาก PLAN เข้าทะเบียนจริง หลังไฟล์ JSON ออกและผ่านสามด่านแล้ว ──
    #    (check_k2 65 ข้อ 0 จุด · ด่าน 7 หนี้ใหม่ 0 ข้อ · audit44 สะสม 74 ข้อ 0 ปัญหา)
    #    ป้ายทั้งห้าแถวย้ายมาตรงตัว ไม่มีการแก้ป้ายระหว่างย้ายในก้อนนี้
    'q070': ('G-TRI-THREE-SIDES-NUM',        'A-COS-OF-LARGEST-ANGLE', 'M-LAW-COS'),
    'q071': ('G-SPECIAL-ANGLES-RADIAN-EXPR', 'A-EXPR-VALUE',           'M-SPECIAL-ANGLE-SUBST'),
    'q072': ('G-TRI-SAS-WITH-MIDPOINT',      'A-SEGMENT-LEN',          'M-LAWCOS-ON-SUB-TRIANGLE'),
    'q073': ('G-POLE-TWO-GROUND-OBS-RIGHTANGLE', 'A-HEIGHT',           'M-TWO-RIGHT-TRI-PLUS-PYTHAG-IN-PLANE'),
    'q074': ('G-TRI-SIDES-GEOMETRIC-SEQ',    'A-ANGLE-RANGE-SET',      'M-LAWCOS-AMGM-RANGE'),
    # ── ก้อน 14 · ย้ายจาก PLAN เข้าทะเบียนจริง หลังไฟล์ JSON ออกและผ่านสามด่านแล้ว ──
    #    (check_k2 70 ข้อ 0 จุด · ด่าน 7 หนี้ใหม่ 0 ข้อ · audit44 สะสม 79 ข้อ 0 ปัญหา)
    #    ป้ายทั้งห้าแถวย้ายมาตรงตัว ไม่มีการแก้ป้ายระหว่างย้ายในก้อนนี้
    'q075': ('G-LADDER-ON-WALL-LEN-ANGLE',     'A-HEIGHT',            'M-RIGHT-TRI-SINE-DIRECT'),
    'q076': ('G-EQ-TAN-SCALED-ARG',            'A-MAX-SOLUTION',      'M-WINDOW-EXPAND-TWO-BRANCH-SELECT'),
    'q077': ('G-RAMP-SAME-HEIGHT-TWO-ANGLES',  'A-LENGTH-DIFFERENCE', 'M-SHARED-HEIGHT-SINE-TWICE'),
    'q078': ('G-EQ-NESTED-TRIG-ARG',           'A-SOLUTION-SET',      'M-BOUND-INNER-THEN-INTEGER-CASES'),
    'q079': ('G-HIGH-EVEN-POWER-SUM-EQ-CONST', 'A-COUNT-SOLUTIONS',   'M-MINIMUM-EQUALITY-CASE'),
    # ── ก้อน 15 · ย้ายจาก PLAN เข้าทะเบียนจริง หลังไฟล์ JSON ออกและผ่านสามด่านแล้ว ──
    #    (check_k2 75 ข้อ 0 จุด · ด่าน 7 หนี้ใหม่ 0 ข้อ · audit44 สะสม 84 ข้อ 0 ปัญหา)
    #    ป้ายทั้งห้าแถวย้ายมาตรงตัว ไม่มีการแก้ป้ายระหว่างย้ายในก้อนนี้
    'q080': ('G-DOUBLE-ANGLE-VALUE-GIVEN',     'A-RATIO-VALUE',         'M-DOUBLE-REVERSE'),
    'q081': ('G-ARC-SPECIAL-POS-ARGS',         'A-EXPR-VALUE',          'M-ARC-PRINCIPAL-VALUE-SUM'),
    'q082': ('G-TAN-SUM-AND-ONE-TAN',          'A-SINE-OF-OTHER-ANGLE', 'M-TAN-DIFF-REVERSE-REF-TRI'),
    'q083': ('G-IDENTITY-EQUATION-SEC-TAN',    'A-EXPR-VALUE',          'M-PYTHID-CONJ'),
    'q084': ('G-TRI-TWO-SIDES-AREA-INSCRIBED', 'A-ARC-LEN',             'M-AMBIG-ANGLE-2R-CENTRAL-ARC'),
    # ── ก้อน 16 · ย้ายจาก PLAN เข้าทะเบียนจริง หลังไฟล์ JSON ออกและผ่านสามด่านแล้ว ──
    #    (check_k2 80 ข้อ 0 จุด · ด่าน 7 หนี้ใหม่ 0 ข้อ · audit44 สะสม 89 ข้อ 0 ปัญหา)
    #    ป้ายทั้งห้าแถวย้ายมาตรงตัว ไม่มีการแก้ป้ายระหว่างย้ายในก้อนนี้
    'q085': ('G-ARCCOS-LINEAR-COMBINATION',    'A-RANGE',             'M-PRINCIPAL-RANGE-AFFINE-MAP'),
    'q086': ('G-CLOCK-TWO-HANDS-LENGTHS-TIME', 'A-DIST-BETWEEN-TIPS', 'M-HAND-ANGLE-THEN-LAW-COS'),
    'q087': ('G-COS-SUM-AND-COS-DIFF',         'A-TAN-PRODUCT',       'M-SPLIT-SUMDIFF-RATIO'),
    'q088': ('G-TRI-TWO-SIDES-INCLUDED-ANGLE', 'A-BISECTOR-LEN',      'M-AREA-SPLIT-HALF-ANGLE'),
    'q089': ('G-ROPE-AT-BUILDING-CORNER',      'A-AREA',              'M-THREE-SECTORS-DIFF-RADII'),
    # ── ก้อน 17 · ย้ายจาก PLAN เข้าทะเบียนจริง หลังไฟล์ JSON ออกและผ่านสามด่านแล้ว ──
    #    (check_k2 85 ข้อ 0 จุด · ด่าน 7 หนี้ใหม่ 0 ข้อ · audit44 สะสม 94 ข้อ 0 ปัญหา)
    #    ป้ายทั้งห้าแถวย้ายมาตรงตัว ไม่มีการแก้ป้ายระหว่างย้ายในก้อนนี้
    #    ⭐ ก้อนแรกที่เนื้อข้อ 4 ใน 5 แต่งขนานด้วยตัวช่วย — ด่านทั้งสามยังผ่านครบ ⇒ วิธีนี้ใช้ได้จริง
    'q090': ('G-NUM-COS2-MINUS-SIN2',            'A-EXPR-VALUE',      'M-DOUBLE-COLLAPSE-EVAL'),
    'q091': ('G-RATIONAL-TRIG-EXPR',             'A-EQUIVALENT-EXPR', 'M-FACTOR-PYTHID-CANCEL'),
    'q092': ('G-HORIZONTAL-CYLINDER-WATER-DEPTH', 'A-VOLUME',         'M-SEGMENT-AREA-TIMES-LENGTH'),
    'q093': ('G-POLE-SHADOW-ON-SLOPE',           'A-SHADOW-LEN',      'M-OBLIQUE-TRI-LAW-SIN'),
    'q094': ('G-SECTOR-ROLLED-INTO-CONE',        'A-VOLUME',          'M-ARC-TO-CIRCUMFERENCE-PYTHAGORAS'),
    # ── ก้อน 18 · ย้ายจาก PLAN เข้าทะเบียนจริง หลังไฟล์ JSON ออกและผ่านสี่ด่านแล้ว ──
    #    (check_k2 95 ข้อ 0 จุด · ด่าน 7 หนี้ใหม่ 0 ข้อ · audit44 สะสม 104 ข้อ 0 ปัญหา
    #     · ด่าน ④ crossnew.py 45/45 คู่ ตก 0 คู่)
    #    ป้ายทั้งสิบแถวย้ายมาตรงตัว ไม่มีการแก้ป้ายระหว่างย้ายในก้อนนี้
    #    ⭐ ก้อนแรกที่ขยายเป็น 10 ข้อ (คำสั่ง ② ของจดหมาย E→MB #20) และแต่งขนาน 5 ข้อรวดเดียว
    'q095': ('G-SECTOR-ARC-ANG',        'A-RADIUS',           'M-SECTOR-FORMULAS'),
    'q096': ('G-PRODUCT-TRIG-EXPR',     'A-EQUIVALENT-EXPR',  'M-EXPAND-TO-SINCOS-CANCEL'),
    'q097': ('G-TWO-RATIOS-TWO-QUAD',   'A-SIN-OF-SUM',       'M-SIGN-BY-QUADRANT-THEN-SUM'),
    'q098': ('G-GABLE-ROOF-PITCH',      'A-SHEET-AREA',       'M-RAFTER-BY-COSINE-THEN-RECT'),
    'q099': ('G-SIN-AND-QUADRANT',      'A-EXPR-VALUE',       'M-DOUBLE-ANGLE-COLLAPSE-TO-TAN'),
    'q100': ('G-RATIONAL-TRIG-SUM',     'A-EQUIVALENT-EXPR',  'M-COMMON-DENOM-SYMMETRIC-COLLAPSE'),
    'q101': ('G-LINEAR-SIN-COS-QUAD',   'A-RECIPROCAL-VALUE', 'M-REF-TRIANGLE-WITH-SIGN'),
    'q102': ('G-QUAD-IN-COSINE',        'A-COUNT-SOLUTIONS',  'M-FACTOR-QUAD-COUNT-BRANCHES'),
    'q103': ('G-EQ-SIN-EQUALS-COS',     'A-MIN-POSITIVE-SOL', 'M-COFUNCTION-TWO-FAMILIES'),
    'q104': ('G-BALLOON-TWO-TETHERS',   'A-DISTANCE-BETWEEN', 'M-HEIGHT-THEN-COSINE-LAW'),
    # ── ก้อน 19 (q105-q124) · ย้ายเข้า REG 8 ส.ค. 69 ───────────────────
    # 🔻 **ย้ายช้าไป 3 วัน — หนี้บัญชีที่ผมเพิ่งเจอเอง**
    #   ก้อน 19 ขึ้นคลังตั้งแต่ 5 ส.ค. 69 (q105-q124 อยู่ใน gen-chap-07 ครบ 20 ข้อ
    #   ยืนยันด้วยการอ่านไฟล์ชุด ⛔ ไม่ใช่จากใบส่งงาน) แต่แถวทั้ง 20 ยังค้างใน PLAN
    #   ⇒ REG มี **144 แถว** ⛔ ไม่ใช่ 164 · เลข 164 ที่ผมเคยพูด คือ REG+PLAN รวมกัน
    #   ⇒ ป้ายผิดแบบเดียวกับ ㊳ : เลขถูก แต่บอกไม่ครบว่าเป็นเลขของกองไหน
    #   ก้อน 20 กับ 21 เข้า REG ตรง ๆ ไม่ผ่าน PLAN ⇒ ช่องว่างนี้เลยไม่มีใครสะดุด
    'q105': ('G-SEC-VALUE-ACUTE',               'A-RATIO-VALUE',    'M-PYTHID-DIRECT'),
    'q106': ('G-RIGHT-TRI-LEG-RATIO-PERIMETER', 'A-SIDE-LEN',       'M-SCALE-FACTOR-PYTHAG'),
    'q107': ('G-RIGHT-TRI-SIDES-IN-X',          'A-RATIO-VALUE',    'M-PYTHAG-QUADRATIC-SOLVE'),
    'q108': ('G-TWO-NESTED-RIGHT-TRI-SHARED-LEG', 'A-SEGMENT-LEN',  'M-TWO-TANGENTS-SHARED-LEG'),
    'q109': ('G-RIGHT-TRI-ANGLE-BISECTOR',      'A-BISECTOR-LEN',   'M-HALF-ANGLE-TAN-IN-RIGHT-TRI'),
    'q110': ('G-RIGHT-TRI-ALTITUDE-TO-HYP',     'A-RATIO-VALUE',    'M-SIMILAR-RIGHT-TRIANGLES'),
    'q111': ('G-REGULAR-POLYGON-INSCRIBED',     'A-PERIMETER',      'M-CENTRAL-ANGLE-HALF-CHORD'),
    'q112': ('G-TRAPEZOID-TWO-BASE-ANGLES-LEGS', 'A-AREA',          'M-DROP-TWO-ALTITUDES-TAN'),
    'q113': ('G-SECTOR-R-ARC',                  'A-AREA',           'M-HALF-R-TIMES-ARC'),
    'q114': ('G-SECTOR-AREA-ARC',               'A-ANGLE-RADIAN',   'M-ELIMINATE-RADIUS'),
    'q115': ('G-TWO-SECTORS-EQUAL-AREA',        'A-RADIUS',         'M-EQUATE-AREAS-SOLVE-RADIUS'),
    'q116': ('G-CIRCLE-ARCS-RATIO-3POINTS',     'A-ARC-LEN',        'M-RATIO-OF-FULL-TURN'),
    'q117': ('G-SECTOR-INSCRIBED-CIRCLE',       'A-RADIUS',         'M-INSCRIBED-CIRCLE-IN-SECTOR'),
    'q118': ('G-SECTOR-R-ANG',                  'A-ARC-MINUS-CHORD', 'M-ARC-AND-CHORD-HALF-ANGLE'),
    'q119': ('G-SECTOR-SCALE-RADIUS-FIXED-AREA', 'A-ARC-RATIO',     'M-AREA-INVARIANT-SCALING'),
    'q120': ('G-FUNC-FORM',                     'A-AMPLITUDE',      'M-READ-COEFFICIENT'),
    'q121': ('G-FUNC-FORM',                     'A-PERIOD-DEGREE',  'M-PERIOD-FROM-COEFF'),
    'q122': ('G-FUNC-VALUE-AT-POINT',           'A-EXPR-VALUE',     'M-EVALUATE-DIRECT'),
    'q123': ('G-GRAPH-KEY-POINTS-TABLE',        'A-EQUATION',       'M-MATCH-PERIOD-AND-SHIFT'),
    'q124': ('G-GRAPH-MAX-MIN-POSITIONS',       'A-COEFF-VALUE',    'M-HALF-PERIOD-FROM-MAX-TO-MIN'),
    # ── ก้อน 20 (6 ส.ค. 69) ────────────────────────────────────────────
    'q125': ('G-RIGHT-TRI-MIDSEGMENT-AND-LEG',   'A-RATIO-VALUE',   'M-MIDSEGMENT-DOUBLE-TO-HYPOTENUSE'),
    'q126': ('G-RIGHT-TRI-SIN-HYP-INCIRCLE',     'A-RADIUS',        'M-INRADIUS-RIGHT-TRI-AREA-OVER-S'),
    'q127': ('G-RIGHT-TRI-SIDES-AP-AREA',        'A-PERIMETER',     'M-AP-SIDES-FORCE-3-4-5'),
    'q128': ('G-RIGHT-TRI-MEDIAN-AND-AREA',      'A-EXPR-VALUE',    'M-MEDIAN-HALF-HYP-SYMMETRIC-SUM'),
    'q129': ('G-RIGHT-TRI-INSCRIBED-SQUARE-PERI', 'A-RATIO-VALUE',  'M-INSCRIBED-SQUARE-THEN-BRANCH-PICK'),
    'q130': ('G-TWO-CIRCLES-EQUAL-CENTRAL-ANGLE', 'A-ARC-RATIO',    'M-EQUAL-CENTRAL-ANGLE-ARC-PROPORTION'),
    'q131': ('G-SECTOR-WITH-CHORD-TRIANGLE',     'A-AREA-RATIO',    'M-SECTOR-TRIANGLE-AREA-RATIO'),
    'q132': ('G-THREE-EQUAL-CIRCLES-TANGENT',    'A-RADIUS',        'M-TANGENT-CIRCLES-CENTRAL-REGION-ARC-SUM'),
    'q133': ('G-SQUARE-TWO-QUARTER-DISCS-OPP',   'A-AREA',          'M-TWO-QUARTER-DISCS-INCLUSION-EXCLUSION'),
    'q134': ('G-THREE-SEMICIRCLES-SPLIT-DIAM',   'A-SEGMENT-LEN',   'M-SEMICIRCLES-ON-SPLIT-DIAMETER-SOLVE-PART'),
    'q135': ('G-UC-NONSTANDARD-START-ARC',       'A-EXPR-VALUE',    'M-ARC-FROM-NONSTANDARD-START'),
    'q136': ('G-UC-POINT-AT-SHIFTED-PARAM',      'A-EXPR-VALUE',    'M-QUARTER-TURN-BOTH-DIRECTIONS'),
    'q137': ('G-HALFTURN-ABSCOS-PRODUCT-SIGN',   'A-EXPR-VALUE',    'M-COLLAPSE-PRODUCT-TO-SINGLE-SIGN'),
    'q138': ('G-SUBARC-ACROSS-TWO-QUADRANTS',    'A-EXPR-VALUE',    'M-SUBQUADRANT-ARC-PICKS-BRANCH'),
    'q139': ('G-PIECEWISE-TRIG-TWO-BRANCHES',    'A-EXPR-VALUE',    'M-PIECEWISE-BRANCH-SELECT'),
    'q140': ('G-FUNC-PRODUCT-SHIFTED-ARGS',      'A-SUM-MAX-MIN',   'M-COFUNCTION-PRODUCT-TO-SQUARE'),
    'q141': ('G-ABS-EQ-PARAM-SOLUTION-COUNT',    'A-PARAM-VALUE',   'M-ABS-TWO-BRANCH-ROOT-COUNT'),
    'q142': ('G-TAN-VALUE-GIVEN',                'A-EXPR-VALUE',    'M-DIVIDE-BY-COS-TO-TAN'),
    'q143': ('G-EQ-SINE-CONJUGATE-FRACTION',     'A-EXPR-VALUE',    'M-CONJ-SINE-PAIR-THEN-EXTRANEOUS-ROOT'),
    'q144': ('G-RECIP-SQUARES-SUM-SUBINTERVAL',  'A-EXPR-VALUE',    'M-RECIP-SQUARES-TO-TAN-QUAD-ROOT-PICK'),
    # ── ก้อน 21 (7 ส.ค. 69) ────────────────────────────────────────────
    'q145': ('G-RIGHT-TRI-SINCOS-SUM',          'A-EXPR-VALUE',   'M-SQUARE-SUM-SINCOS-TO-PRODUCT'),
    'q146': ('G-RIGHT-TRI-SIDES-GP',            'A-RATIO-VALUE',  'M-GP-SIDES-QUADRATIC-IN-RATIO-SQ'),
    'q147': ('G-RIGHT-TRAPEZOID-THREE-SIDES',   'A-RATIO-VALUE',  'M-RIGHT-TRAPEZOID-DROP-PERP'),
    'q148': ('G-RIGHT-TRI-TWO-HYP-LEG-DEFICITS', 'A-RATIO-VALUE', 'M-TWO-DEFICITS-QUAD-POSITIVITY'),
    'q149': ('G-QUAD-TWO-OPPOSITE-RIGHT-ANGLES', 'A-EXPR-VALUE',  'M-SHARED-HYP-AREA-SPLIT-SYM-TAN'),
    'q150': ('G-WHEEL-RADIUS-REVOLUTIONS',      'A-ROLL-DISTANCE', 'M-ROLL-REVOLUTIONS-TO-DISTANCE'),
    'q151': ('G-SECTOR-RADIUS-GROWS-ARC-DELTA', 'A-AREA-DELTA',   'M-ARC-INCREMENT-TO-ANGLE-THEN-AREA'),
    'q152': ('G-WIPER-INNER-OUTER-RADIUS-ANGLE', 'A-AREA',        'M-ANNULAR-SECTOR-SWEPT-AREA'),
    'q153': ('G-SQUARE-FOUR-SEMICIRCLES-BULGE',  'A-AREA',        'M-BALANCED-BULGE-INDENT-CANCEL'),
    'q154': ('G-SECTOR-FIXED-PERI-RADIUS-CAP',  'A-EXTREME',      'M-FIXED-PERI-SECTOR-MAX-AT-CAP'),
    'q155': ('G-UC-TWO-ARCS-SUM-PI',            'A-EXPR-VALUE',   'M-ARC-PAIR-SUM-PI-ABSCISSA-PRODUCT'),
    'q156': ('G-POINT-PARAM-ON-AXIS',           'A-COORD-VALUE',  'M-POINT-ON-AXIS-FROM-PARAM'),
    'q157': ('G-TWO-ARCS-SUM-3PI-OVER-2',       'A-EXPR-VALUE',   'M-ARC-SUM-CROSS-CONDITION-SIGN'),
    'q158': ('G-CSC-OVER-COT-AND-SIGN',         'A-EXPR-VALUE',   'M-AP-QUARTER-SUM-CYCLE-CANCEL'),
    'q159': ('G-FOUR-TRIG-FUNCTIONS-LIST',      'A-IDENTIFY-PARITY', 'M-ODD-EVEN-PARITY-TEST'),
    'q160': ('G-COMPOSITE-TRIG-IN-TRIG',        'A-EXTREME',      'M-COMPOSITE-INNER-RANGE-THEN-OUTER'),
    'q161': ('G-RATIONAL-PRODUCT-DENOM-TRIG',   'A-SUM-MAX-MIN',  'M-PRODUCT-DENOM-EXPAND-PYTH-RANGE'),
    'q162': ('G-TAN-PLUS-COT-VALUE',            'A-EXPR-VALUE',   'M-TAN-PLUS-COT-TO-RECIP-PRODUCT'),
    'q163': ('G-IDENTITY-WITH-UNKNOWN-CONSTANT', 'A-COEFF-VALUE', 'M-EXPAND-SQUARES-RECIP-PYTH-CONST'),
    'q164': ('G-WEIGHTED-QUARTIC-SUM-CONDITION', 'A-EXPR-VALUE',  'M-WEIGHTED-POWER-PERFECT-SQ-FORCE'),
}

# ═══════════════════════ ของที่ถอนไปแล้ว · เก็บไว้เป็นชุดทดสอบ ═══════════════════════
# ถ้าเปิดใช้ ตัวตรวจต้องจับ q040เก่า ↔ q025 ให้ได้ มิฉะนั้นแปลว่าด่านเสีย
RETIRED = {
    'q040เก่า(ถอน)': ('G-FUNC-FORM',    'A-PERIOD',         'M-LCM-PERIOD'),
}

# ═══════════════════════ แผนของก้อนถัดไป · เติมตรงนี้ก่อนแต่ง ═══════════════════════
# ก้อน 8 · ฉบับออกแบบใหม่ทั้งก้อน (แม่พิมพ์ชุดแรกตายหมด 5 อันจาก collide_b8.py)
# ⭐ ทุกแถวผ่านการกวาดคลัง 6,357 ข้อ ด้วย collide_b8b.py + collide_b8c.py แล้ว
#    q045 เงื่อนไขเครื่องหมาย⇒จตุภาค : กวาดแล้ว 0 ข้อ · คำว่า “จตุภาคใด” ทั้งคลังมีข้อเดียว
#                                     คือ q041 ของเราเอง (G, M ต่างกัน)
#    q046 เรียงลำดับค่าของมุมเรเดียน : กวาดแล้ว 0 ข้อ · ทั้งคลังไม่มีมุมเรเดียนล้วนที่ไม่มี pi
#    q047 แบบจำลองไซน์ในโลกจริง      : กวาดแล้ว 0 ข้อ · บท 7.10 ทั้งคลังมีแต่มุมก้ม/มุมเงย
#                                     กับเข็มนาฬิกา ไม่มีแบบจำลองคาบเลยสักข้อ
#    q048 ช่วงที่เป็นฟังก์ชันเพิ่ม      : 5 ข้อในคลัง เป็นบท 13 (อนุพันธ์) ทั้งหมด
#                                     บทที่ 7 มีข้อเดียวคือ q134 ซึ่งเป็นแบบตัดสินข้อความ
#    q049 ให้จำนวนจุดตัด ⇒ ถอดค่า b   : กวาดแล้ว 0 ข้อที่เป็นตรีโกณ
# ═══ ก้อน 9 · q050-q054 · เจาะ 7.8 (ยังไม่มีสักข้อ) + 7.9 ที่ยังบาง ═══
#    ผลกวาด (collide_b9.py · collide_b9b.py · ฐาน 6,362 ข้อ)
#    ทั้งคลังมีข้อที่เอ่ยฟังก์ชันผกผัน 114 ข้อ (บท 7 เอง 55 · ป้าย 7.8 รวม 75)
#    แม่พิมพ์ที่ "อิ่มตัวแล้ว" ⇒ ห้ามแตะ : คิดค่านิพจน์ arc ซ้อน (19) · ผลบวก arctan (14) ·
#                                        สมการ arcsin+arccos (หลายข้อ) · มุมเงยสองจุดสังเกต (8)
#    q050 ค่าสุดขีดของ (arcsin)^2+(arccos)^2 : กวาดแล้ว 0 ข้อ · ทั้งคลังไม่มี arc ยกกำลังสองเลย
#    q051 เรียงลำดับค่าของ arc              : กวาดแล้ว 0 ข้อ · การพับช่วงหลักมี 4 ข้อ แต่ถาม "ค่า" ทุกข้อ
#    q052 โดเมนของ arcsin ที่ข้างในเป็นกำลังสอง: 5 ข้อที่มีรูปนี้ แต่ทุกข้อถาม "คำตอบของสมการ" ไม่ใช่โดเมน
#    q053 SSA กรณีกำกวมจริง                 : กวาดแล้ว 0 ข้อที่ใช้ประโยชน์จากความกำกวม
#                                            (q111 ตั้งใจเลี่ยงด้วยการถาม sin3B ซึ่งเท่ากันทั้งสองรูป)
#    q054 สี่เหลี่ยมมุมตรงข้ามรวม 180 · 4 ด้าน: 1 ข้อ (alvl1-2566-03-q06) แต่ให้มุมมาแล้วถามด้าน
# ═══ ก้อน 10 · q055-q059 · เจาะ 7.5 / 7.6 / 7.7 ที่ยังบางที่สุด (4 / 4 / 3 ข้อ) ═══
#    ผลกวาด (collide_b10.py · collide_b10b.py · ฐาน 6,367 ข้อ)
#    แม่พิมพ์ที่ "อิ่มตัวแล้ว" ⇒ ทิ้งไป 3 อันตั้งแต่รอบแรก :
#       ผลบวกของคำตอบสมการตรีโกณ (77 ข้อ) · ผลคูณโคไซน์ยุบมุมสองเท่า (12 ข้อ) ·
#       a sin x + b cos x = c แบบมุมช่วย (80 ข้อ)
#    ทิ้งเพิ่มรอบสอง : sin3x + sinx = sin2x ⇒ ชนกับ chap-07-q59 และ pat1-2557-03-q36 ที่ให้
#       สมการเดียวกันเป๊ะ (sin A - sin 2A + sin 3A = 0) ⇒ เปลี่ยนเป็นหลักการ sin A = sin B
#    ทิ้งเพิ่มรอบสอง : "ให้ sin theta + จตุภาค ⇒ หาค่านิพจน์ครึ่งมุม" ⇒ ใกล้ pat1-2559-10-q11
#       มากเกินไป ⇒ กลับทิศเป็น "ให้ค่านิพจน์ครึ่งมุม ⇒ หา cos theta" แทน
#    q055 สัมประสิทธิ์ของเอกลักษณ์ที่จริงทุก x : ทั้งคลังมี 1 ข้อ และเป็นบท 3 (pat1-2554-03-q49)
#    q056 กลับทิศครึ่งมุม                      : กวาดแล้ว 0 ข้อ
#    q057 sin ax = sin bx สองสาขา + คำตอบซ้ำ    : ใกล้ที่สุดคือ samn-2565-03-q26 ซึ่งเป็น
#                                                sin 5theta = 3/4 (สาขาเดียว ไม่มีคำตอบซ้ำ)
#    q058 ให้ sin(A+B) กับ sin(A-B) ⇒ อัตราส่วน tan : กวาดแล้ว 0 ข้อที่ให้ทั้งคู่พร้อมกัน
#    q059 พารามิเตอร์ในสมการกำลังสองของ cos x + คุมจำนวนคำตอบเป๊ะ ๆ : ใกล้ที่สุดคือ gen-q005
#                                                ซึ่งเป็น sin x และถามแค่ "มีคำตอบ" ไม่ใช่ "กี่คำตอบ"
#    ── ปรับ q059 รอบสาม (collide_b10c.py) ──────────────────────────────────────
#    ให้คะแนน rubric ของ q059 ฉบับเดิม (2cos^2 x + (2a-1)cos x - a = 0) ตามจริงได้ 11 = ยาก
#    ครูสั่งว่าทุกก้อนต้องมี "ยากมาก" และย้ำว่า "ยากมากเป็นผลผลิตของวิธีแต่ง ไม่ใช่คุณสมบัติของบท"
#    ⇒ ออกแบบใหม่ให้ยากขึ้นจริง : เขียนโจทย์เป็น cos 2x + (2a-1)cos x + (1-a) = 0
#      เด็กต้องเลือกสูตรมุมสองเท่ารูป cos เอง (cos 2x มีสามรูป · เลือกผิดจะได้สมการปน sin กับ cos)
#      ⛔ ไม่ใช่การดันคะแนนของข้อเดิม — ให้คะแนนใหม่หลังเปลี่ยนโจทย์แล้ว
#      กวาดชนแล้ว : cos 2x ปนกับ cos x + พารามิเตอร์ = 0 ข้อ · ที่ใกล้ที่สุดคือ pat1-2559-10-q34
#      (cos 2x + sin x = tan 225° · ไม่มีพารามิเตอร์ ไม่ได้ถามจำนวนคำตอบ) และ gen-chap-03-real-q031
#      (|x^2-6x+8| = k มีคำตอบพอดี 3) ซึ่งเป็นแนวนับเหมือนกันแต่คนละบทคนละกลไกทั้งหมด
# ── ก้อน 11 (q060–q064) · หลักฐานการกวาด collide_b11.py + collide_b11b.py ────────
#    ฐานเทียบ 6,372 ข้อ (คลัง 62 ชุด + ที่แต่งเองแล้ว 59 ข้อ)
#    ทิศของก้อน : สะสม 59 ข้อได้ ง่าย 12 (20%) · ปานกลาง 22 (37%) · ยาก 15 (25%) · ยากมาก 10 (17%)
#      เทียบเป้า 25/35/25/15 ⇒ "ง่าย" ขาด ⇒ ก้อนนี้เอนไปทางง่าย 3 + ยาก 1 + ยากมาก 1
#      ⛔ ไม่ใช่การเอาข้อยากมาลดตัวเลข — เลือกแม่พิมพ์ที่ตื้นโดยธรรมชาติตั้งแต่ต้น
#    ✅ ช่องว่างที่ยืนยันแล้ว (0 ข้อ)
#       A2 ให้ส่วนโค้ง + รัศมี ⇒ ถามมุมเป็น "องศา"        = 0  ⇒ q060
#       D3 ให้สองด้าน + มุมระหว่าง ⇒ พื้นที่ (แบบตรง)      = 1 (เป็นข้อเวกเตอร์) ⇒ q061
#       B1 มุมร่วมปลาย                                    = 1 (q020 ของเราเอง · คนละเครื่องมือ) ⇒ q062
#       N1 เงื่อนไขรูป a cos A = b cos B                   = 3 (ไม่มีข้อไหนถามชนิดของรูป) ⇒ q063
#       I1 ตัดสินชนิดของรูปสามเหลี่ยมจากเอกลักษณ์          = 0  ⇒ q063
#       G1/O1 ด้านเรียงแบบลำดับเลขคณิต                     = 0  ⇒ q064
#    ⛔ แม่พิมพ์ที่กวาดแล้วอิ่มตัว ⇒ ทิ้งทั้งหมด
#       C1 คู่มุมประกอบ/โคฟังก์ชัน                = 84 ข้อ
#       E1 พื้นที่ segment (เซกเตอร์ − สามเหลี่ยม) = 13 ข้อ · ตรงตัว chap-07-q107 · q212 · q217
#       H1 เซกเตอร์เส้นรอบรูปคงที่ ⇒ พื้นที่มากสุด = ตรงเป๊ะกับ chap-13-calculus-q97
#       J1 มุมก้ม-มุมเงย-เข็มนาฬิกา               = 23 ข้อ
#       F1 เส้นมัธยฐาน : รอบแรกได้ 137 ข้อ แต่เป็น "มัธยฐาน" ของสถิติทั้งหมด ⇒ กวาดใหม่เฉพาะบท 7
#          (F2) ได้ 7 ข้อ เป็น "จุดกึ่งกลาง" ของเรขาคณิตล้วน ⇒ แม่พิมพ์นี้ยังว่างจริง (เก็บไว้ก้อนหน้า)
#       L1 ความเร็วเชิงมุม/ล้อหมุน/รอก/สายพาน     = 1 (chap-13-calculus-q108) ⇒ ว่าง แต่ทำให้ q060
#          กลายเป็น "ปานกลาง" (L=1) ซึ่งสวนทางกับทิศของก้อน ⇒ เก็บไว้ก้อนหน้า
#    หมายเหตุ q064 : ในก้อนนี้เคยออกแบบข้อ "ด้านอัตราส่วน 3:5:7" ไว้อีกข้อหนึ่ง แต่ถอนออก
#       เพราะสองข้อในก้อนเดียวกันใช้แม่พิมพ์ "ด้านเรียงเลขคณิต" เหมือนกัน = ซ้ำในก้อน
#    (ก้อน 11 ย้ายเข้า REG แล้ว 5 ส.ค. 69 หลังผ่าน check_k2 · ด่าน 7 · audit44)
# ── ก้อน 12 · แม่พิมพ์ที่ "กวาดไว้แล้วว่าว่าง" และกันไว้ให้ก้อนนี้โดยเฉพาะ ─────────
#    ⭐ สองอันนี้ผ่านการกวาดใน collide_b11b.py แล้ว ไม่ต้องกวาดซ้ำ แต่ต้องกวาดอันใหม่ที่เพิ่มเข้ามา
#    F2 เส้นมัธยฐาน/จุดกึ่งกลางด้าน ในบทตรีโกณ = 7 ข้อ ล้วนเป็นเรขาคณิตพิกัด ⇒ ว่างจริง
#    L1 ความเร็วเชิงมุม/ล้อหมุน/รอก/สายพาน     = 1 ข้อ (chap-13-calculus-q108) ⇒ ว่างจริง
#       และมี L=1 โดยธรรมชาติ ⇒ ออกมาเป็น "ปานกลาง" ซึ่งตรงกับทิศที่ก้อน 12 ต้องการพอดี
#    ทิศของก้อน 12 (จาก grade_b11.py) : สะสม 64 ข้อได้ ง่าย 23.4% · ปานกลาง 34.4% ·
#       ยาก 25.0% · ยากมาก 17.2% ⇒ ควรเป็น ง่าย 2 + ปานกลาง 3 และ ⛔ ไม่เติมยากมาก
#       ⇒ แต่คำสั่งครู E→MB #19 ข้อ ④ บังคับว่าทุกก้อนต้องมี "ยากมาก" ⇒ ยึดคำสั่งครู
#    ⛔ สองข้อที่ถูกฆ่าในรอบกวาดที่สาม (collide_b12c.py) — ทั้งคู่ชนกับ "ข้อที่เราแต่งเอง"
#       q065 ฉบับ 1 (ให้ด้าน ⇒ ถาม sec A − tan A)  ชน gen-chap-07-trigonometry-q007
#       q068 ฉบับ 1 (ให้ค่าสูงสุด-ต่ำสุด-คาบ ⇒ a+b+c) ชน gen-chap-07-trigonometry-q009
#    ⛔ q068 ฉบับ 2 (สองเมืองบนเมริเดียนเดียวกัน ⇒ ระยะตามผิว) ถอนเองในรอบสี่
#       เพราะ A (ความยาวส่วนโค้ง) และ M (แปลงองศาแล้ว s = r·theta) ตรงกับ q033 ลูกตุ้ม
#       ⇒ จะกลายเป็น WATCH-A ทั้งที่เลี่ยงได้ ⇒ เปลี่ยนเป็นฉบับ 3 (เส้นละติจูด = วงกลมเล็ก)
#       ฉบับ 3 ต้องหารัศมีวงกลมละติจูด R·cos(phi) ก่อน ⇒ M ใหม่จริง (กวาดยืนยันแล้ว 0 ข้อ)
# ── ก้อน 13 (q070–q074) · กวาด 14 รอบ (collide_b13.py … collide_b13p.py) ─────────
#    ⚠️ ก้อน 13 ให้เอียงคำตอบมาช่อง 1 (สะสม 69 ข้อได้ 16/18/18/17 — ช่อง 1 ต่ำสุด)
#       ⇒ ก้อนนี้ลงช่อง 1,4,1,3,2 ⇒ สะสมใหม่ 18/19/19/18 (กระจายที่สุดเท่าที่ทำได้)
#    ⛔ แม่พิมพ์ที่ถูกฆ่าในก้อนนี้ = 26 อัน (มากที่สุดตั้งแต่เริ่มโครงการ) · ห้าอันหลังสุด
#       ชนกับ "ข้อที่เราแต่งเอง" ทั้งหมด ⇒ เป็นสัญญาณว่าที่ว่างของแม่พิมพ์ในบทที่ 7 ตีบลงจริง
#       ① แบบจำลองน้ำขึ้นน้ำลง d(t)=7+4sin(pi t/6) ⇒ ชน q047 (ชิงช้าสวรรค์ · A+M ตรง)
#       ② SSA กำกวม b=8 A=pi/6 ⇒ ผลบวกด้านที่สาม ⇒ ชน q053 ของเราเอง (สมการกำลังสองตัวเดียวกัน)
#       ③ พิสัยของนิพจน์ arcsin+arccos ⇒ ชน q050 ของเราเอง (ทั้งหัวข้อ 7.8 ตันในก้อนนี้)
#       ④ เซกเตอร์เส้นรอบรูปคงที่ ⇒ พื้นที่มากสุด ⇒ ชน q034 ของเราเอง + chap-13-calculus-q97
#       ⑤ tan alpha, tan beta เป็นรากของสมการกำลังสอง ⇒ alpha+beta ⇒ ชน chap-07-q182 (G+M)
#          และ samn-2559-12-q03 (A) ⇒ ล้อมทั้งสองแกน
#    ✅ หลักฐานว่าห้าแถวข้างล่างว่างจริง (ฐานเทียบ 6,382 ข้อ · ยิงตรงแบบไม่กรองบท)
#       q070 ให้สามด้านเป็นตัวเลขล้วน ⇒ cos ของมุมตรงข้ามด้านยาวสุด : R1a/R1b/X6 = 0
#       q071 นิพจน์มุมพิเศษในรูปเรเดียนล้วน ⇒ ค่าตัวเลข          : R2b = 0 · q071-B (13/2) = 0
#       q072 จุดกึ่งกลางด้าน + กฎโคไซน์ในสามเหลี่ยมย่อย          : F2-แคบ/R5/Q4/X4 = ไม่มีข้อไหน
#            เป็นเส้นมัธยฐานจริง (ทุกข้อเป็น "จุดกึ่งกลาง" ของเรขาคณิตพิกัด)
#       q073 เสาตั้งฉากพื้นราบ + ผู้สังเกตสองจุดที่ทำมุมฉากกันที่ฐาน : A4 (ลายเซ็น 45+30+มุมฉาก) = 0
#            ⚠️ A1/A2/A3 ได้ 2/6/6 ข้อ ตรวจด้วยตาแล้วทุกข้อเป็นแม่พิมพ์ "เดินตรงเข้าหาฐาน"
#            (q100 q102 q202 q203 q206 pat1-2564-03-q17 q22 และ q003 ของเราเอง) ⇒ G และ M คนละตัว
#       q074 ด้านสามด้านเป็นลำดับเรขาคณิต ⇒ เซตของขนาดมุม B      : R4a/R4b/U3/Q6 = 0
#    📌 ก้อน 14 ต้องเลี่ยง 7.9 (ก้อนนี้ใช้ไป 3 ข้อ) และ 7.8 (ตัน) ⇒ เล็ง 7.7 (5) · 7.1 (6→7)
#       แม่พิมพ์ที่ยังกันไว้และยืนยันว่าว่าง : บันไดพาดกำแพง (B1=B2=B3=0) · เงายาว (W4) ·
#       ทางลาด (W5) · กลับทิศเส้นมัธยฐาน/อพอลโลเนียส (X4)
#    ✅ ก้อน 13 ย้ายเข้า REG แล้ว (ดูบล็อก "ก้อน 13" ด้านบน) ⇒ PLAN ว่างรอก้อน 14
#
# ── ⚠️ บันทึกเฉียดฉิว q073 ↔ chap-07-trigonometry-q102 (พบตอนกวาดก้อน 14 รอบ 3) ──
#    q102 : "สุดายืนทางทิศตะวันออกของตึก มุมเงย 45 องศา · เดินไปทางทิศใต้ 100 ม.
#            มุมเงยเหลือ 30 องศา ⇒ ความสูงของตึก"  ตอบ 50√2
#    q073 : เสาธงที่ O · ผู้สังเกต A, B โดย ∠AOB เป็นมุมฉาก · มุมเงย 45 กับ 30 · AB = 24
#    ผิวเผินเหมือนกันมาก แต่ "มุมฉากอยู่คนละจุด" ⇒ สมการคนละสมการ
#       q073 มุมฉากที่ O (โคนเสา)      ⇒ AB² = OA² + OB² = h² + 3h² ⇒ h = 12
#       q102 มุมฉากที่ A (จุดสังเกตแรก) ⇒ OB² = OA² + AB² = h² + 10000 ⇒ h = 50√2
#    ⭐ ตัวลวง 12√2 ของ q073 คือเส้นทางพลาด "วางด้านตรงข้ามมุมฉากผิดข้าง" ซึ่ง = รูปทรงของ q102 พอดี
#       ⇒ สองข้อ "เติมเต็มกัน" ไม่ใช่ซ้ำกัน · ตัดสิน: ⚠️ WATCH-A · ผ่านกฎเหล็กข้อ 5 · q073 คงไว้
#    🔴 บทเรียนที่ต้องทำต่อ (กฎโพรบใหม่ · ใช้กับ 7.10 ทุกข้อจากนี้ไป):
#       โพรบก้อน 13 ยิงหาคำว่า "มุมฉาก"/"มุม AOB"/"90 องศา" ⇒ มองไม่เห็น q102
#       เพราะ q102 เข้ารหัสมุมฉากด้วย "ทิศ" (ตะวันออก → ใต้) ไม่ใช่คำว่ามุมฉาก
#       ⇒ ต้องกวาดด้วย (ก) คำบอกทิศ ทิศเหนือ/ใต้/ตะวันออก/ตะวันตก
#          (ข) รูปทรง = "มุมฉากอยู่ที่จุดยอดไหน" ไม่ใช่คำศัพท์
# ── ก้อน 14 (q075–q079) · กวาด 3 รอบ (collide_b14 / b14b / b14c) ──────────────────
#    ⛔ ฆ่าแบบร่างไป 7 อัน : C sin x+cos x=ค่าคงที่ (25 ข้อ) · D sin3x=cos2x นับคำตอบ (ชน q057)
#       · E sin⁴+cos⁴=a (ชน q055) · H สมการเอกพันธ์⇒กำลังสองใน tan (ชน chap-07-q147 เต็ม ๆ)
#       · tan α,tan β เป็นรากสมการกำลังสอง (chap-07-q182 · pat1-2561-02-q07 · q001)
#    ✅ หลักฐานว่าห้าแถวข้างล่างว่าง : บันได A1=16 ข้อ (false positive ทั้งหมด · A'2=0 ในบท 7)
#       · B'2=0 · B'3=1 (บท 3 เท่านั้น) · F'1=1 (pat1-2564-03-q17 คนละแม่พิมพ์) · F'2=0
#       · K1 ตรีโกณซ้อนตรีโกณ = 0 ข้อจากฐาน 6,387 · J1=4 ข้อ ใกล้สุด chap-07-q145
#         (sin⁶+cos⁶=1/4 ถามผลบวก ⇒ ต่างทั้ง A · M · ตัวเลข)
#    ✅ ก้อน 14 ย้ายเข้า REG แล้ว (ดูบล็อก "ก้อน 14" ด้านบน) ⇒ PLAN ว่างรอก้อน 15
#    📌 ก้อน 15 ต้องเลี่ยง 7.7 (ก้อนนี้ใช้ไป 3 ข้อ ⇒ สะสม 8) และ 7.2 (สะสม 20 สูงสุด)
#       ⇒ เล็ง 7.5 (8) · 7.6 (8) · 7.8 (4 · ตันเรื่องแม่พิมพ์ ต้องกวาดหนัก) · 7.11 (8)
#    ⚠️ โควตาระดับสั่งว่าก้อน 15 ต้องมีข้อ "ง่าย" จริง ๆ อย่างน้อย 2 ข้อ (แถบ ง่าย เหลือ 22.8%)
#       และ "ยากมาก" 1 ข้อตามคำสั่ง ④ (ยากมาก ต้องมีทุกก้อน)
# ── ก้อน 15 (q080–q084) · กวาด 4 รอบ (collide_b15 / b15b / b15c / b15d) ─────────────
#    ⛔ ฆ่าแบบร่างไป 4 อัน :
#       (1) P1b (ค่า sin/cos ของมุมสองเท่าจากอัตราส่วนที่ให้) ชน q016
#       (2) P3a (เรียงลำดับค่า arc) ชน q051 ของเราเอง
#       (3) q080 ฉบับแรก (1 - 2 sin^2 75 องศา ⇒ cos 150) — โพรบถ้อยคำได้ 0 ข้อ **แต่**
#           ทะเบียนขึ้น WATCH-B สองคู่ (q012 ↔ q080 · q016 ↔ q080 ที่ G-ANG-NUMERIC +
#           A-EXPR-VALUE) และ q016 ใช้มุม 75 องศาเหมือนกันเป๊ะ ⇒ ต่างกันแค่แกน "ตัวเลข"
#           แกนเดียว ผิดเจตนากฎเหล็กข้อ 5 ⇒ เปลี่ยน G (สิ่งที่โจทย์ให้) ไม่ใช่แค่เปลี่ยนเอกลักษณ์
#           หลักฐานรอบ 4 (out_b15d.txt) : M1 ไปข้างหน้า = 25 ข้อ (แน่น) · M2 ย้อนกลับ = 3 ข้อ
#           (ไม่ใช่แม่พิมพ์เดียวกันสักข้อ) · M3 = 4 ข้อ มี q017 ของเราเอง ⇒ เลือก M2
#       (4) q083 ฉบับแรก (คอนจูเกต sec-tan แบบ "หาค่านิพจน์") — ให้คะแนน rubric ตรง ๆ ได้
#           F2 C1 P0 T2 L0 = 5 ⇒ ปานกลาง ไม่ใช่ ยาก ⛔ ไม่ยอมปั๊มคะแนนให้ตรงแผน
#           (ยึดบรรทัดฐาน q075 ในก้อน 14) ⇒ ออกแบบใหม่เป็น "สมการ" ที่มีกุญแจดอกที่สอง
#           (ยกกำลังสองแล้วต้องตรวจรากแปลกปลอม) จึงถึง 8 ได้อย่างซื่อสัตย์
#       (5) q084 ฉบับแรก (ให้ b c และมุม A = 60 องศา ⇒ ความยาวส่วนโค้ง) — ให้คะแนนตรง ๆ ได้
#           F3 C2 P2 T2 L1 = 10 ⇒ "ยาก" ไม่ถึง "ยากมาก" ⛔ ไม่ยอมดัน L เป็น 2 ทั้งที่รูปเป็น
#           ระนาบเดียว (บรรทัดฐาน q077 : ระนาบเดียว ⇒ L=1) และไม่ยอมดัน T เป็น 3
#           ⇒ ทำตามคำสั่ง ④ ตรง ๆ : "ยากมาก" เป็นผลผลิตของ **วิธีแต่ง** ⇒ แต่งให้ยากขึ้นจริง
#           โดยไม่ให้มุม A มาตรง ๆ แต่ให้ "พื้นที่" แทน ⇒ sin A = sqrt3/2 ⇒ A มีสองค่าใน
#           สามเหลี่ยม (60 กับ 120 องศา) ⇒ ต้องคำนวณ BC ทั้งสองกิ่งก่อน จึงใช้เงื่อนไข
#           BC < AB คัดกิ่งได้ ⇒ ได้กิ่งจริง + กุญแจดอกที่สาม อย่างซื่อสัตย์
#    ✅ หลักฐานว่าห้าแถวข้างล่างว่าง (ฐานเทียบ 6,392 ข้อ) :
#       q080  M2 (ให้ cos 2t เป็นค่า ⇒ ถอยกลับหา sin t) = 3 ข้อ ไม่ใช่แม่พิมพ์เดียวกัน
#             · M4 = 0 · M5 = 0 · A1/A2/A3 = 0
#       q081  B1 · B2 (arcsin+arccos ในคำถามเดียว) = 0 · q081-1/2/3 = 0
#             ⚠️ จงใจให้อาร์กิวเมนต์ของ arccos กับ arcsin "ต่างกัน" (1/2 กับ sqrt3/2) เพื่อไม่ให้
#             เอกลักษณ์ arcsin x + arccos x = pi/2 ใช้ได้ ⇒ เด็กต้องอ่านค่าหลักของแต่ละตัวเอง
#             ⚠️ ใช้อาร์กิวเมนต์ "บวก" ทั้งคู่ (ไม่ใช่ลบตามร่างเดิม) เพราะอาร์กิวเมนต์ลบทำให้
#             ช่วงค่าหลักกลายเป็นกุญแจจริง ⇒ T=1 ⇒ ตกไปเป็นปานกลาง แต่ก้อนนี้ต้องการ ง่าย 2 ข้อ
#       q082  C1 (ให้ tan(A+B) เป็นค่า) = 0 · q082-2 (ให้ tan มุมหนึ่ง ถาม sin อีกมุม) = 0
#       q083  D3 (1/(sec-tan) - 1/(sec+tan)) = 0 · F1 (sec^2-tan^2 ในคำถาม) = 0
#             ⚠️ ญาติใกล้สุดคือ q007 ของเราเอง (sec A - tan A = 1/3 ⇒ sin A) — เครื่องมือ
#             ตั้งต้นเดียวกันจริง จึงจดป้าย M เป็น 'M-PYTHID-CONJ' ตัวเดิม ไม่เลี่ยงป้าย
#             แต่ G ต่าง (ให้ "สมการ" ไม่ใช่ค่า) และ A ต่าง (ค่า sin+cos ไม่ใช่ sin เดี่ยว)
#       q084  ⛔ ฉบับแรก (ให้มุม A = 60 องศามาตรง ๆ) ถูกฆ่าด้วยเหตุที่ (5) ด้านล่าง
#             ฉบับแก้กวาดรอบ 5 (out_b15e.txt) : N1 = 1 ข้อ (เป็นเรขาคณิตสามมิติ บท 9)
#             · N6 (เงื่อนไขเทียบด้าน BC < AB) = 0 · N2/N3/N4/N5/N7 มีของ แต่ไล่ดูทุกข้อแล้ว
#             ญาติใกล้สุดคือ chap-07-q122 (พื้นที่ + มุม 60 องศา ⇒ ด้านที่สั้นที่สุด) — ให้มุมมา
#             ตรง ๆ ไม่มีการแตกกิ่ง และถามความยาวด้าน ไม่ใช่ส่วนโค้ง ⇒ ต่างครบทั้งสามแกน
#             และ q069 ของเราเอง (BC=6 · A=pi/3 ⇒ ช่วงของเส้นรอบรูป) ⇒ คนละ A คนละ M
#    📌 ก้อน 15 เลี่ยง 7.7 และ 7.2 ตามที่ก้อน 14 สั่งไว้ ⇒ ลง 7.6 · 7.8 · 7.5/7.1 · 7.4 · 7.9/7.11
#       (7.8 เป็นหัวข้อย่อยที่บางที่สุดของเรา — มีแค่ 4 ข้อจาก 79 ⇒ q081 ปิดช่องว่างจริง)
#    ✅ โควตา : ง่ายจริง 2 ข้อ (q080 q081) · ยากมาก 1 ข้อ (q084) ตามคำสั่ง ④
#    ✅ ก้อน 15 ย้ายเข้า REG แล้ว (ดูบล็อก "ก้อน 15" ด้านบน) ⇒ PLAN ว่างรอก้อน 16
#    📌 ก้อน 16 ต้องเลี่ยง 7.2 (สะสม 20 สูงสุด) · 7.3 (17) · 7.9 (12)
#       ⇒ เล็ง 7.8 (5 · บางสุด) · 7.10 (8) · 7.5 (9) · 7.6 (9) · 7.7 (9) · 7.11 (9)
#       ⚠️ 7.2 · 7.3 เป็นเป้าลำดับต้นตามคำสั่ง ③ ของจดหมาย E→MB #19 — แต่สะสมสูงสุดแล้ว
#          ⇒ ใส่ได้ในฐานะหัวข้อ "เสริม" (subTopic ที่สอง) ไม่ใช่แกนหลักของข้อ
#    ⚠️ โควตาระดับหลังก้อน 15 : ง่าย 23.8 · ปานกลาง 34.5 · ยาก 23.8 · ยากมาก 17.9
#       ⇒ ก้อน 16 ควรเป็น ง่าย 1 · ปานกลาง 2 · ยาก 1 · ยากมาก 1 (ยากมาก ต้องมีทุกก้อนตามคำสั่ง ④)
#    ✅ หลักฐานว่าห้าแถวข้างล่างว่าง (ฐานเทียบ 6,397 ข้อ · กวาด 5 รอบ b16 · b · c · d · e) :
#       q085  R1 · เรนจ์ของ a·arccos x + b — R1a ไม่มีข้อบทตรีโกณเลย · arccos 34 ข้อ และ
#             "สัมประสิทธิ์หน้า arc" 23 ข้อ เป็นแม่พิมพ์ "หาค่านิพจน์" ทั้งหมด ไม่มีข้อไหนถามเรนจ์
#       q086  R2 · คำว่า "เข็ม" ทั้งคลังเจอข้อเดียว = pat1-2552-10-q22 ซึ่งถาม "มุมระหว่างเข็ม"
#             ⇒ A ต่าง · M ต่าง (ข้อนั้นไม่ใช้กฎโคไซน์เลย)
#       q087  S3 · S3a ชนเดียว = chap-07-q108 (โจทย์สามเหลี่ยม G ต่าง) · S3b = 0
#       q088  V1 · V1g (แบ่งสามเหลี่ยมเป็นสองรูปแล้วบวกพื้นที่) = 0 ข้อทั้งคลัง
#             ⚠️ ญาติใกล้สุด chap-09-vector-q98 (AB:AC = BP:PC ⇒ AP เป็นเส้นแบ่งครึ่งจริง)
#             แต่ G ต่าง (ให้อัตราส่วน+ความยาวเส้นเชียน) · A ต่าง (ถาม cos(A/2)) · M ต่าง (เวกเตอร์)
#       q089  T1 · T1a 7 ข้อไม่เกี่ยว · T1b 1 ข้อไม่เกี่ยว · T1c = 0
#    ⛔ ที่ถูกฆ่าระหว่างทาง : R3 R4 R5 R6 R7 · S18 · T2 · U5 U7 U8 U10 · V2 V3 V4 (S9 พักไว้)
#    ✅ ก้อน 16 ย้ายเข้า REG แล้ว (ดูบล็อก "ก้อน 16" ด้านบน) ⇒ PLAN ว่างรอก้อน 17
#    📌 ก้อน 17 ต้องเลี่ยง 7.2 (สะสม 20 สูงสุด) · 7.3 (17) · 7.9 (14 · ขึ้นมาจากก้อน 16)
#       ⇒ เล็ง 7.8 (6 · บางสุด) · 7.7 (9) · 7.10 (9) · 7.1 (10) · 7.5 (10) · 7.6 (10) · 7.11 (10)
#    ⚠️ โควตาระดับหลังก้อน 16 : ง่าย 23.6 · ปานกลาง 34.8 · ยาก 23.6 · ยากมาก 18.0
#       ⇒ แถบ "ยากมาก" แตะขอบ +3.0 pp พอดี · ก้อน 17 ต้องเป็น ง่าย 2 · ยาก 2 · ยากมาก 1
#          (ยากมาก ยังต้องมีทุกก้อนตามคำสั่ง ④ แต่ต้องมีของถ่วงคู่มาด้วย)
#    ⚠️ ช่องคำตอบสะสม 21/24/23/21 ⇒ ก้อน 17 ควรเอนไปช่อง 1 กับ 4 (ผ่านการเรียงค่าจริง ไม่ใช่จัดฉาก)
#    ✅ หลักฐานว่าห้าแถวก้อน 17 ว่าง (ฐานเทียบ 6,402 ข้อ · กวาด 3 รอบ b17 · b · c) :
#       q090  E1 · 4 ข้อที่มี cos^2-sin^2 ไม่มีข้อไหนเป็นแม่พิมพ์ "ยุบแล้วคิดค่า"
#             ⛔ ร่างแรก (sin75 cos15 - cos75 sin15) ถูกฆ่าเพราะซ้ำ q016 ของเราเองแบบคำต่อคำ
#             ⇒ บทเรียน : ก่อนออกแบบ "ง่าย" ต้องกวาดคลังของตัวเองก่อน ไม่ใช่กวาดแต่คลังเดิม
#       q091  N2 · N2d (เศษ-ส่วนเป็นพหุนามดีกรีสามของ sin/cos) = 0 · N2e 1 ข้อไม่เกี่ยว
#       q092  N3 · N3b2 (ถังนอนราบ + ความลึกน้ำ) = 0 · ญาติใกล้สุด chap-07-q107 ต่างครบสามแกน
#       q093  N4 · คำว่า "เงา" ในความหมายเงาแดด ไม่ปรากฏเลยทั้ง 6,402 ข้อ
#             ญาติใกล้สุด chap-07-q224 ต่างที่ G และ A
#             ⚠️ regex รอบแรกให้ผลลวง 3 จุด (เนิน↔ดำเนินการ · เงา↔แรเงา · กรวย↔ภาคตัดกรวย)
#             ⇒ แก้เป็น (?<!แร)เงา(?!ื) · (?<!ภาคตัด)กรวย · (?<!ดำ)เนินเขา
#       q094  N5 · N5b2 (ม้วนเซกเตอร์เป็นกรวย) = 0 · คำว่า "กรวย" 47 ข้อเป็นภาคตัดกรวย/แคลคูลัสหมด
#    ✅ ก้อน 17 ย้ายเข้า REG แล้ว (ดูบล็อก "ก้อน 17" ด้านบน) ⇒ PLAN ว่างรอก้อน 18
#    📌 ก้อน 18 เป็น "ก้อน 10 ข้อ" ก้อนแรก ตามมติครูเรื่องความเร็ว (ขยาย 5 ⇒ 10 · แต่งขนาน)
#       ⇒ ยังส่งไฟล์ JSON ให้ครูทุก 5 ข้อเหมือนเดิม
#    📌 ก้อน 18 ต้องเลี่ยง 7.2 (สะสม 20 สูงสุด) · 7.3 (17) · 7.9 (15 · ขึ้นมาจากก้อน 17)
#       ⇒ เล็ง 7.8 (6 · บางสุด) · 7.7 (9) · 7.5 (10) · 7.10 (10) · 7.6 (11)
#    ⚠️ โควตาระดับหลังก้อน 17 : ง่าย 24.5 · ปานกลาง 33.0 · ยาก 24.5 · ยากมาก 18.1
#       ⇒ "ยากมาก" หลุดกรอบ +3.1 pp แล้ว (เกิน ±3) · ส่งเรื่องให้ครูเคาะใน CHANGELOG ก้อน 17
#       ⇒ ระหว่างรอคำเคาะ ก้อน 18 (10 ข้อ) ให้เป็น ง่าย 2 · ปานกลาง 6 · ยาก 1 · ยากมาก 1
#          (ปานกลางขาดมากสุด -2.0 pp ⇒ ต้องเติมหนัก · ยากมาก 1 ใน 10 = 10% จะดึงแถบลงเอง)
#    ⚠️ ช่องคำตอบสะสม 22/25/26/21 ⇒ ก้อน 18 ควรเอนไปช่อง 4 (ผ่านการเรียงค่าจริง ไม่ใช่จัดฉาก)
#    ✅ ก้อน 18 ย้ายเข้า REG แล้ว (ดูบล็อก "ก้อน 18" ด้านบน) ⇒ PLAN ว่างรอก้อน 19
#
# ── ก้อน 19 (q105-q124) · 20 ข้อ · ลำดับเติมตามคำสั่งครู 7.1 -> 7.11 -> 7.3 ──────────
#    แผนนี้ผ่านการกวาดชน 3 รอบใน session ก่อน (ตาย 7 แม่พิมพ์) แล้ว "แช่แข็ง" ไว้ในใบส่งงาน
#    ⛔ ห้ามกวาดซ้ำ ⛔ ห้ามเปลี่ยนแม่พิมพ์ — session นี้รับแผนมาเขียนโจทย์อย่างเดียว
#    ⛔ ห้ามใช้ M-SECTOR-FORMULAS (ใช้ไปแล้ว 6 ครั้ง มากที่สุดในทะเบียน)
#       ⇒ ทั้งเจ็ดข้อของ 7.11 ในก้อนนี้ใช้เครื่องมือคนละตัวกันหมด
# ── ก้อน 22 (q165-q184) · ลงทะเบียน 8 ส.ค. 69 · **15 แถว ⛔ ไม่ใช่ 20** ──────────
#
# 🔴 ทำไมได้ 15 : กวาดชนกับ **คลังจริงทั้ง 63 ชุด 6,477 ข้อ** (`collide_b22.py`)
#    แล้วเจอว่า 5 ข้อชนของเดิม ⇒ **ถอนออกจากแผน รอออกแบบใหม่** (รายละเอียดล่างสุด)
#
# 🔴 และนี่คือรูของด่านนี้เอง (㊸) : REG รู้จักแค่ **164 ข้อที่เราแต่งเอง**
#    ⇒ ด่านนี้ **มองไม่เห็นอีก 6,313 ข้อในคลัง** โดยเฉพาะชุดข้อสอบจริง
#    ⇒ q165 (ชน `samn-2559-12-q03`) และ q174 (ชน `alvl1-2566-03-q07`)
#       **ผ่านด่านนี้แบบเขียว** ทั้งที่ซ้ำของจริง ⇒ `collide_b22.py` ⛔ ไม่ใช่ของเสริม
#
# 📌 ㊳ (หน่วย/ขอบเขตของตัวเลข) : ใบสั่งงานก้อน 22 เล็ง "หัวข้อบางสุด" จากตัวเลข
#    **ของชุดเราเอง** (7.8 = 6 ข้อ) แต่ตัวเลขที่ควรใช้ตอนหาที่ว่างของแม่พิมพ์คือ
#    **ของทั้งคลัง** (7.8 = 73 ข้อ · มากที่สุดในบท) ⇒ เล็งเข้าที่แน่นที่สุดพอดี
#    วัดเอง 8 ส.ค. 69 · นับ subTopics[0] · บท 7 ทั้งคลัง 529 ข้อ / ชุดเรา 164 ข้อ :
#        หัวข้อ   ชุดเรา  ทั้งคลัง        หัวข้อ   ชุดเรา  ทั้งคลัง
#        7.1        26       27           7.7        9       55
#        7.2        22       41           7.8        6       73  ← บางสุดของเรา = แน่นสุดของคลัง
#        7.3        26       41           7.9       12       63
#        7.4        13       46           7.10       8       45
#        7.5         6       53           7.11      28       31
#        7.6         8       54
# ═════════════════ 🪧 แฟ้มกักกัน · PLAN_ORPHANED ═════════════════
# 15 แถวข้างล่างนี้คือ **ร่องรอยชิ้นสุดท้ายของก้อน 22** — เนื้อหาของทั้ง 20 ข้อหายไปแล้ว
# (⬤ ยืนยัน 2 ที่ 8 ส.ค. 69: ทั้งคอนเทนเนอร์และเครื่องครูไม่มี k2/b22/ และ k2/parts_b22/)
#
# 🔴 ทำไมต้องย้ายออกจาก `PLAN` ⛔ ไม่ใช่ปล่อยไว้ — วัดเองแล้วทั้งสองข้อ (ของล่อ C·D · ใบ #46):
#   D : แถวเหล่านี้ **ปฏิเสธ** ข้อของก้อนถัดไปที่บังเอิญใช้แม่พิมพ์เดียวกัน (q172 ↔ qB23TEST)
#   C : ทันทีที่คลังโตขึ้น 1 ข้อ ใบเสร็จของทั้ง 15 แถว **หมดอายุพร้อมกัน** ⇒ ด่านแดงค้าง
#   ⇒ ⇒ ทางออกเดียวที่เหลือคือ "กวาดใหม่" ของที่ไม่มีเนื้อหาให้กวาด
#        = งานที่ทำไม่ได้ กลายเป็นเงื่อนไขของการเดินต่อ ⇒ ⑯ (ด่านที่แดงเสมอ = ด่านที่ถูกปิด)
#
# ⛔ **ห้ามลบแถวเหล่านี้** — คำสั่งผูกพัน "ห้ามลบบันทึกเก่า" (retired = ถอนค่า เก็บโครง)
# ⛔ **ห้ามอ้างแฟ้มนี้เป็นของจริง** — ⛔ ไม่ใช่ทะเบียน ⛔ ไม่ใช่แผน · มีด่านเฝ้า (selftest ⑫⑬⑭)
# 🔑 ย้ายกลับเข้า `PLAN` ได้เสมอถ้าวันหนึ่งแต่งเนื้อหาขึ้นมาใหม่ — และน้ำหนักจะกลับมาทันที
#
# ⬤ 🎣 E ยืนยันว่าการย้ายนี้ตัดน้ำหนักออกจริง (8 ส.ค. 69 · รันเอง):
#     แม่พิมพ์ตรงกับแถวในแฟ้มกักกัน ⇒ ปล่อย (exit 0) · แถวเดิมอยู่ใน PLAN ⇒ ปฏิเสธ (exit 1)
#     คลังโต 1 ข้อ ⇒ "ใบเสร็จหมดอายุ" เหลือ 0 id
PLAN_ORPHANED = {
    # ── 7.5 ──
    'q166': ('G-ANG-NUMERIC',                'A-EXPR-VALUE',        'M-SPLIT-INTO-TWO-SPECIAL-ANGLES'),
    'q167': ('G-TAN-OF-SUM-AND-DIFF-VALUES', 'A-TAN-OF-DOUBLE',     'M-REGROUP-2A-AS-SUM-PLUS-DIFF'),
    'q169': ('G-COS-SUM-AND-COS-PRODUCT',    'A-TAN-PRODUCT',       'M-EXPAND-COS-SUM-ONCE'),
    'q170': ('G-THREE-TAN-VALUES',           'A-TAN-OF-TRIPLE-SUM', 'M-TAN-SUM-CHAINED-TWICE'),
    # ── 7.8 ──
    'q172': ('G-TRIG-OF-TWO-SEPARATE-ARCS',  'A-EXPR-VALUE',        'M-RIGHT-TRI-FROM-ARC-ARG'),
    'q175': ('G-ARCTAN-PAIR-FUNCTION-OF-X',  'A-IDENTIFY-VALUE-SET', 'M-BRANCH-BY-PRINCIPAL-RANGE'),
    'q176': ('G-ARC-EQUATION-DOUBLE-ARCTAN', 'A-SOLUTION-VALUE',    'M-SIN-OF-DOUBLE-ARCTAN'),
    # ── 7.10 ──
    'q177': ('G-CABLECAR-SLOPE-TAN-GIVEN',   'A-HEIGHT',            'M-TAN-TO-SIN-VIA-TRIPLE'),
    'q178': ('G-POLE-HEIGHT-AND-SHADOW-FLAT', 'A-ANGLE-DEGREE',     'M-TAN-RATIO-TO-SPECIAL-ANGLE'),
    'q179': ('G-TRI-SAS-NUMERIC-FIELD',      'A-SIDE-LEN',          'M-LAW-COS'),
    'q180': ('G-ANTENNA-ON-ROOF-TWO-ELEVATIONS', 'A-HEIGHT-DIFFERENCE', 'M-TWO-TANGENTS-SHARED-LEG'),
    # ── 7.7 ──
    'q181': ('G-EQ-BASIC',                   'A-SUM-ROOTS',         'M-TWO-ROOTS-IN-FULL-TURN'),
    'q182': ('G-QUAD-IN-SINE',               'A-SUM-ROOTS',         'M-FACTOR-QUAD-SUM-ALL-ROOTS'),
    'q183': ('G-EQ-SIN-PLUS-COS-CONST',      'A-COUNT-SOLUTIONS',   'M-SQUARE-THEN-REJECT-EXTRANEOUS'),
    'q184': ('G-EVEN-POWER-SUM-EQ-PRODUCT',  'A-SUM-ROOTS',         'M-POWER-REDUCE-TO-SIN2X-QUADRATIC'),
}

# ═══════ 5 ข้อที่ถอนออกจากแผนก้อน 22 · รอออกแบบใหม่ (⛔ ไม่ลงทะเบียน) ═══════
#   ทุกบรรทัดวัดเอง 8 ส.ค. 69 จาก `data/sets/*.json` 63 ชุด 6,477 ข้อ
#
#   🔴 q165  tan A = 1/3, tan B = 1/2 (แหลม) ⇒ A + B
#            ชน `samn-2559-12-q03` (**ข้อสอบจริง** วิชาสามัญ 2559) :
#            "tan A = 2 และ tan B = 3 แล้ว A + B" — **แม่พิมพ์เดียวกัน พื้นผิวเดียวกัน**
#            ต่างแค่ตัวเลข ⇒ 1 ใน 3 แกน ⇒ ผิดกฎเหล็กข้อ 5
#
#   🔴 q171  arctan 1 + arctan √3
#            ชน `gen-chap-07-trigonometry-q081` (ของเราเอง) :
#            "arccos(1/2) + arcsin(√3/2)" — ผลบวกค่าอาร์กสองตัวที่อาร์กิวเมนต์พิเศษ
#            เปลี่ยนแค่ชื่อฟังก์ชันอาร์ก = แกนตัวเลข ⇒ 1 ใน 3 แกน
#            (และ "ผลบวก arctan" อยู่ในรายการแม่พิมพ์อิ่มตัวของ `collide_b19.py` อยู่แล้ว)
#
#   🔴 q173  arcsin(sin 11π/6)
#            ชน `gen-chap-07-trigonometry-q051` (เป็นชิ้นส่วน a ของข้อนั้นพอดี)
#            และ `pat1-2562-02-q06` (**ข้อสอบจริง** PAT1 ก.พ. 2562)
#            ⛔ และแม่พิมพ์ "arcsin(sin x) นอกช่วงหลัก" **ถูกฆ่าไปแล้วตั้งแต่ก้อน 12**
#            (บันทึกใน CHANGELOG ก้อน 12) ⇒ ข้อนี้ไม่ควรถูกออกแบบตั้งแต่แรก
#
#   🔴 q174  tan(arcsin(3/5) + arccos(5/13)) = −63/16
#            ชน `alvl1-2566-03-q07` (**ข้อสอบจริง** A-Level 2566) :
#            "tan(arccos(5/13) + arcsin(3/5))" — **ตัวเลขชุดเดียวกัน คำตอบเดียวกัน**
#            (−63/16 เป็นตัวเลือกที่ 1 ของข้อสอบจริงนั้นด้วย) ต่างแค่ลำดับพจน์
#            ⇒ นี่ ⛔ ไม่ใช่แค่แม่พิมพ์ชน — เป็น**ข้อเดียวกันกับข้อสอบจริง**
#
#   🟠 q168  sin A = 5/13 (จตุภาค 2), tan B = 3/4 (จตุภาค 3) ⇒ sin(A − B)
#            ชน `gen-chap-07-trigonometry-q097` (ของเราเอง) :
#            sin A = 3/5 (จตุภาค 2), cos B = −12/13 (จตุภาค 3) ⇒ sin(A + B)
#            G เดียวกัน · M เดียวกัน · สามเหลี่ยมมุมฉากชุดเดียวกัน (3-4-5 กับ 5-12-13)
#            ต่างที่ A อย่างเดียว (ผลบวก ↔ ผลต่าง) ⇒ ด่านนี้จะขึ้นแค่ ⚠️ WATCH-A
#            **แต่ตามกฎเหล็กข้อ 5 (ต่าง 2 ใน 3 แกน) ข้อนี้ตก** ⇒ ถอนไว้ให้ครูเคาะ
#
# 🟠 สองข้อที่ **ไม่ถอน** แต่ต้องบันทึกว่าใกล้ :
#   q169 ↔ `gen-chap-07-q087`  ถามค่าเดียวกัน (tan A tan B) สำนวนใกล้กัน
#         **แต่โจทย์ให้คนละอย่าง** (q087 ให้ cos ผลบวก+ผลต่าง · q169 ให้ cos ผลบวก
#         + cos A cos B) และเส้นทางสั้นกว่าหนึ่งขั้น ⇒ ต่าง 2 ใน 3 แกน ⇒ ผ่าน
#   q176 ↔ ตระกูล "2·อาร์ก" ในคลังมี **23 ข้อ** (วัดเอง) รวม `chap-07-q186`
#         ที่ใช้ `2 arctan(1/3)` เป๊ะ **แต่ q176 กลับทิศ** (ให้สมการแล้วหา x)
#         ⇒ ผ่าน แต่ถ้าครูสั่งให้เข้มกว่านี้ ข้อนี้คือข้อถัดไปที่ควรถอน


# ═══════════════════ ชั้น 2+3 · ใบเสร็จการกวาดคลังจริง ═══════════════════
# รูปแบบ: id -> (สคริปต์ที่กวาด, วันที่กวาด, ป้ายตัวหาร ณ วันกวาด)
#
# 🔴 ป้ายตัวหารต้องเป็นค่าที่ **วัดจากคลังจริง** ⛔ ห้ามพิมพ์มือ
#    ได้มาจาก: python3 tools/authoring/k2/bankscope.py
#
# ⚠️ ใบเสร็จ ⛔ ไม่ใช่คำรับรองว่า "ข้อนี้ไม่ซ้ำ" — เป็นคำรับรองว่า
#    "ข้อนี้ถูกเอาไปเทียบกับคลังทั้งใบ ณ สภาพนั้น แล้วมีคนดูผลด้วยตา"
#    (`collide_bNN` พิมพ์ 'เจอของเดิม' ออกมาเพื่อให้คนเปิดดู ⛔ ไม่ได้ตัดสินแทน)
_SCOPE_B22 = '63ไฟล์·6477ข้อ·236d33856a3e3c88'
_B22 = ('collide_b22.py', '2026-08-08', _SCOPE_B22)

RECEIPTS = {
    # ── ก้อน 22 · 15 แถวที่รอด (5 แถวถูกถอนหลังกวาด: q165 q168 q171 q173 q174)
    'q166': _B22, 'q167': _B22, 'q169': _B22, 'q170': _B22,
    'q172': _B22, 'q175': _B22, 'q176': _B22, 'q177': _B22,
    'q178': _B22, 'q179': _B22, 'q180': _B22, 'q181': _B22,
    'q182': _B22, 'q183': _B22, 'q184': _B22,
}

# 🔴 กงล้อ · **ลดได้อย่างเดียว** ⛔ ห้ามเติมชื่อใหม่เข้ารายการนี้เด็ดขาด
#    = 164 แถวที่ลงทะเบียนก่อนกฎใบเสร็จมีอยู่ (q001–q164 · ณ 8 ส.ค. 2569)
#    วิธีปลดชื่อออก: กวาดข้อนั้นด้วย collide ใหม่ แล้วย้ายไปอยู่ใน RECEIPTS
#    ⚠️ ตัวเลข 164 นี้ = `REG` ทั้งก้อน ณ วันตั้งกงล้อ ⛔ ไม่ใช่ REG+PLAN (บทเรียน ㊳)
PRE_RECEIPT_CEILING = 164
PRE_RECEIPT = frozenset('q%03d' % n for n in range(1, PRE_RECEIPT_CEILING + 1))

_BANK_CACHE = []


def require_bank():
    """ชั้น 1 — อ่านคลังทั้งใบ · อ่านไม่ได้ = ตัวตรวจใช้ไม่ได้ (รหัส 2)"""
    if not _BANK_CACHE:
        try:
            _BANK_CACHE.append(bankscope.load_bank())
        except bankscope.BankUnavailable as e:
            print('🔴 ชั้น 1 ล้ม — อ่านคลังจริงไม่ได้ ⇒ **ตัวตรวจใช้ไม่ได้**')
            print('   %s' % e)
            print('   ⛔ ห้ามตีความว่า "ไม่เจอของซ้ำ" — ด่านนี้ยังไม่ได้ตรวจอะไรเลย')
            sys.exit(2)
    return _BANK_CACHE[0]


def check_quarantine(reg, plan, orphaned, quiet=False):
    """ด่านเฝ้าแฟ้มกักกัน — คืนจำนวน ❌

    🔴 ราคาที่ E ระบุไว้ตอนเสนอทาง ค: *"ต้องมีด่านเฝ้าว่าไม่มีใครอ้างแฟ้มกักกันเป็นของจริง"*
       ⇒ ด่านนี้คือราคานั้น ⛔ ไม่ใช่ของแถม
    เฝ้า 2 อย่าง:
      ① id ในแฟ้มกักกันต้องไม่โผล่ใน REG หรือ PLAN พร้อมกัน
         (โผล่พร้อมกัน = มีคนก๊อปกลับเข้าไปโดยไม่ได้ย้ายออก ⇒ ของชิ้นเดียวสองสถานะ)
      ② แฟ้มกักกันต้องไม่ว่างพร้อมกับที่ยังมีใบเสร็จกำพร้าอยู่
         (ว่างทั้งที่มีใบเสร็จ = มีคนลบแถวทิ้ง ⇒ ชน "ห้ามลบบันทึกเก่า")
    """
    bad = []
    both = sorted((set(orphaned) & set(reg)) | (set(orphaned) & set(plan)))
    if both:
        bad.append('id อยู่ทั้งในแฟ้มกักกันและใน REG/PLAN พร้อมกัน: ' + ', '.join(both))
    orphan_receipts = sorted(set(RECEIPTS) - set(reg) - set(plan))
    if orphan_receipts and not orphaned:
        bad.append('มีใบเสร็จกำพร้า %d ใบ แต่แฟ้มกักกันว่าง'
                   ' ⇒ มีคนลบแถวทิ้ง (ชนคำสั่ง "ห้ามลบบันทึกเก่า"): %s'
                   % (len(orphan_receipts), ', '.join(orphan_receipts)))
    if not quiet:
        print()
        print('▼▼▼ 🪧 แฟ้มกักกัน PLAN_ORPHANED ▼▼▼')
        print('  %d แถว — ร่องรอยของก้อน 22 · ⛔ ไม่มีน้ำหนักในการตัดสิน ⛔ ไม่ใช่ของจริง'
              % len(orphaned))
        if bad:
            for m in bad:
                print('❌ ' + m)
        else:
            print('✅ ไม่มีใครอ้างแฟ้มกักกันเป็นของจริง · ไม่มีแถวไหนถูกลบทิ้ง')
    return len(bad)


def check_receipts(reg, plan, bank, quiet=False):
    """ชั้น 2+3 — คืนจำนวน ❌ · id ที่ต้องมีใบเสร็จแล้วไม่มี / ใบเสร็จหมดอายุ"""
    need = [i for i in sorted(plan)]
    need += [i for i in sorted(reg) if i not in PRE_RECEIPT]
    missing, stale = [], []
    for i in need:
        r = RECEIPTS.get(i)
        if r is None:
            missing.append(i)
            continue
        good, why = bankscope.compare_scope(r[2], bank)
        if not good:
            stale.append((i, r, why))
    # ใบเสร็จที่ไม่มีเจ้าของแล้ว = ข้อสังเกต ⛔ ไม่ใช่ ❌ (ของถูกถอนเป็นเรื่องปกติ)
    orphan = sorted(set(RECEIPTS) - set(reg) - set(plan))

    if not quiet:
        print()
        print('▼▼▼ ชั้น 2+3 · ใบเสร็จการกวาดคลังจริง ▼▼▼')
        print('  ตัวหารคลังวันนี้ : %s' % bankscope.scope_str(bank))
        print('  ต้องมีใบเสร็จ %d id (PLAN %d · REG นอกกงล้อ %d)'
              % (len(need), len(plan), len(need) - len(plan)))
        print('  ยกเว้นด้วยกงล้อ PRE_RECEIPT : %d id (ลดได้อย่างเดียว)' % len(PRE_RECEIPT))
        if missing:
            print('❌ ไม่มีใบเสร็จ %d id : %s' % (len(missing), ', '.join(missing)))
        else:
            print('✅ ใบเสร็จครบทุก id ที่ต้องมี')
        if stale:
            print('❌ ใบเสร็จหมดอายุ %d id :' % len(stale))
            for i, r, why in stale:
                print('   %s  กวาดโดย %s เมื่อ %s — %s' % (i, r[0], r[1], why))
        else:
            print('✅ ใบเสร็จทุกใบยังตรงกับคลังวันนี้')
        if orphan:
            print('📌 ใบเสร็จที่เจ้าของถูกถอนไปแล้ว %d ใบ (เก็บไว้เป็นบันทึก ⛔ ไม่ใช่ ❌) : %s'
                  % (len(orphan), ', '.join(orphan)))
    return len(missing) + len(stale)


# ═════════════════ แผนของก้อนถัดไป ═════════════════
# ว่างอยู่ — ก้อน 22 ถูกพักตามมติครู 8 ส.ค. 69 · ก้อน 23 ยังไม่เริ่มออกแบบ
# ⭐ วิธีใช้: เพิ่มบรรทัดของข้อที่จะแต่งลงที่นี่ **พร้อมใบเสร็จใน RECEIPTS** แล้วรันไฟล์นี้
PLAN = {}


def audit(reg):
    keys = sorted(reg)
    fail, watchA, watchB = [], [], []
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            a, b = keys[i], keys[j]
            ga, aa, ma = reg[a]
            gb, ab, mb = reg[b]
            same = (ga == gb) + (aa == ab) + (ma == mb)
            if same == 3:
                fail.append((a, b, reg[a]))
            elif ma == mb and (ga == gb or aa == ab):
                watchA.append((a, b, ma, 'G' if ga == gb else 'A'))
            elif ga == gb and aa == ab:
                watchB.append((a, b, ga, aa, ma, mb))
    return fail, watchA, watchB


def report(title, reg, quiet=False):
    fail, wA, wB = audit(reg)
    if quiet:                      # โหมดชุดทดสอบ · คืนตัวเลขอย่างเดียว ไม่พิมพ์
        return len(fail)
    print('=' * 78)
    print(title, '·', len(reg), 'ข้อ')
    print('=' * 78)
    if fail:
        print('❌ แม่พิมพ์ซ้ำเต็มสามส่วน (ผิดกฎเหล็กข้อ 5) :', len(fail), 'คู่')
        for a, b, t in fail:
            print('   %s ↔ %s' % (a, b))
            print('      G %s' % t[0])
            print('      A %s' % t[1])
            print('      M %s' % t[2])
    else:
        print('❌ แม่พิมพ์ซ้ำเต็มสามส่วน : 0 คู่ ⇒ ผ่าน')
    print()
    print('⚠️  เครื่องมือตรง + อีกหนึ่งส่วนตรง (ต้องตรวจด้วยตา) :', len(wA), 'คู่')
    for a, b, m, ax in wA:
        print('   %s ↔ %s   M=%s  และ %s ตรงกัน' % (a, b, m, ax))
    print()
    print('⚠️  พื้นผิวเหมือน (G+A ตรง) แต่เครื่องมือต่าง :', len(wB), 'คู่')
    for a, b, g, aa, ma, mb in wB:
        print('   %s ↔ %s   G=%s · A=%s   M ต่าง: %s vs %s' % (a, b, g, aa, ma, mb))
    print()
    return len(fail)


# ═══════════════════════ ชุดทดสอบของด่านเอง (㊶) ═══════════════════════
# 🔻 8 ส.ค. 69 · ใบแก้รูรั่วรหัสออก — **ผมเจอเองตอนจะลงทะเบียนก้อน 22**
#   อาการ  : ฉีดแถวที่ชน ❌ เข้า PLAN แล้วรันไฟล์นี้ ⇒ พิมพ์ "❌ 1 คู่" ออกมาจริง
#            **แต่ `echo $?` ได้ 0** เพราะ `nfail` คิดจาก REG อย่างเดียว
#            ค่าที่ report() คืนจากรอบ "ทะเบียน + แผน" ถูกทิ้งทั้งค่า
#   ทำไมถึงร้ายแรงกว่าที่เห็น : docstring บนหัวไฟล์นี้สั่งว่า "ก่อนแต่งข้อใหม่ ให้เพิ่ม
#            บรรทัดของข้อนั้นลง PLAN แล้วรันไฟล์นี้" ⇒ **กรณีใช้งานหลักของไฟล์ คือกรณี
#            ที่คำตัดสินตกหาย** · วันนี้ยังไม่มีสคริปต์ไหนอ่านรหัสออกของไฟล์นี้
#            (กวาดแล้ว 0 จุด) ⇒ **ความเสียหายจริงวันนี้ = 0** ⛔ ไม่ใช่ "ไม่เป็นไร"
#   ยาแก้ที่เลือก : ⛔ ไม่ใช่เขียนเตือนไว้ในคอมเมนต์ — แต่ให้ **รหัสออกมาจากที่เดียว**
#            คือ verdict() ซึ่งบวกทุกกองที่ตรวจ ⇒ ลืมบวกกองใหม่ไม่ได้เชิงโครงสร้าง
#   ㊶ : ตัวตรวจต้องมีชุดทดสอบของตัวเอง ⇒ ของล่อ 2 ตัวข้างล่าง **ตัวที่ 2 คือรูนี้**
_BAIT_REG = ('G-FUNC-FORM', 'A-PERIOD', 'M-LCM-PERIOD')          # = q025 เป๊ะ
_BAIT_PLAN = ('G-TRI-ANY-TANRATIO', 'A-EXPR-VALUE', 'M-TAN-TRI-IDENT')  # = q001 เป๊ะ


def verdict(reg, plan, quiet=False, check_bank=True):
    """รหัสออก = ❌ ของ **ทุกกองที่ตรวจ** ⛔ ไม่ใช่ของ REG อย่างเดียว

    🆕 8 ส.ค. 69 · ชั้น 2+3 บวกเข้ามาที่นี่ ⛔ ไม่ใช่เป็นสคริปต์แยก
       เหตุผลเดียวกับที่ย้ายรหัสออกมาไว้ที่นี่ตอนแรก: กองที่อยู่นอก verdict()
       คือกองที่วันหนึ่งจะมีคนลืมบวก · อยู่ในนี้แล้ว **ลืมไม่ได้เชิงโครงสร้าง**
    check_bank=False ใช้ได้เฉพาะในชุดทดสอบที่ตั้งใจตัดชั้น 1 ออกเพื่อพิสูจน์ว่ามันรับน้ำหนัก
    """
    out = []
    n = report('ทะเบียนปัจจุบัน', reg, quiet)
    out.append(n)
    if plan:
        if not quiet:
            print()
            print('▼▼▼ ตรวจแผนก้อนถัดไป เทียบกับของเดิมทั้งหมด ▼▼▼')
        merged = dict(reg)
        merged.update(plan)
        out.append(report('ทะเบียน + แผน', merged, quiet))
    if check_bank:
        out.append(check_receipts(reg, plan, require_bank(), quiet))
        out.append(check_quarantine(reg, plan, PLAN_ORPHANED, quiet))
    return sum(out)


def selftest():
    """ต้องจับให้ได้ทั้งสองที่ · ต้องปล่อยของสะอาดให้ผ่าน (㊶ ขยาย: มีทั้งเคสจับและเคสปล่อย)"""
    ok = True
    # ① ของล่อใน REG — ของเดิม (q040 ที่ถอนแล้ว) ยังต้องถูกจับ
    t = dict(REG)
    t.pop('q040')
    t.update(RETIRED)
    n1 = verdict(t, {}, quiet=True)
    print('  ① ของล่อใน REG (q040เก่า ↔ q025)      :', 'จับได้ ✅' if n1 else 'หลุด ❌')
    ok &= bool(n1)
    # ② ของล่อใน PLAN — รูที่เจอ 8 ส.ค. 69 · ก่อนแก้ ข้อนี้จะได้ 0
    n2 = verdict(REG, {'qBAIT': _BAIT_PLAN}, quiet=True)
    print('  ② ของล่อใน PLAN (qBAIT ↔ q001)        :', 'จับได้ ✅' if n2 else 'หลุด ❌')
    ok &= bool(n2)
    # ③ เคสที่ต้อง**ปล่อย** — ทะเบียนจริง + แผนจริง ต้องไม่แดง
    n3 = verdict(REG, PLAN, quiet=True)
    print('  ③ ของสะอาด (ทะเบียนจริง + แผนจริง)    :', 'ปล่อยผ่าน ✅' if n3 == 0
          else 'ฟ้องผิด ❌ (%d คู่)' % n3)
    ok &= (n3 == 0)
    # ④ ของล่อ 2 ตัวพร้อมกัน — ต้องนับรวม ⛔ ไม่ใช่รายงานแค่กองแรก
    n4 = verdict(t, {'qBAIT': _BAIT_PLAN}, quiet=True)
    print('  ④ ของล่อพร้อมกันสองกอง                :',
          'นับรวม ✅ (%d)' % n4 if n4 >= 2 else 'นับไม่ครบ ❌ (%d)' % n4)
    ok &= (n4 >= 2)

    # ═══ ชั้น 2+3 · ใบเสร็จ (8 ส.ค. 69) ═══
    bank = require_bank()

    def say(no, name, good):
        nonlocal ok
        print('  %s %-38s : %s' % (no, name, 'ผ่าน ✅' if good else 'ล้ม ❌'))
        ok &= bool(good)

    # ⑤ ของจริงต้องสะอาด — ใบเสร็จครบ + ป้ายตรงคลังวันนี้
    say('⑤', 'ของจริง: ใบเสร็จครบ + ป้ายตรงคลัง',
        check_receipts(REG, PLAN, bank, quiet=True) == 0)

    # ⑥ 🧬 แถวใหม่ใน PLAN ที่ไม่มีใบเสร็จ ⇒ ต้องแดง
    #    (นี่คือเคสของก้อน 22 เป๊ะ: แม่พิมพ์สะอาดในสายตา REG แต่ยังไม่เคยเจอคลังจริง)
    _clean_mold = ('G-ยังไม่เคยมี-เอ', 'A-ยังไม่เคยมี-บี', 'M-ยังไม่เคยมี-ซี')
    say('⑥', '🧬 PLAN ไม่มีใบเสร็จ ⇒ ต้องแดง',
        check_receipts(REG, {'qNOSWEEP': _clean_mold}, bank, quiet=True) >= 1)

    # ⑦ 🧬 แถวใหม่ใน REG (นอกกงล้อ) ที่ไม่มีใบเสร็จ ⇒ ต้องแดง
    _r7 = dict(REG)
    _r7['q900'] = _clean_mold
    say('⑦', '🧬 REG นอกกงล้อ ไม่มีใบเสร็จ ⇒ ต้องแดง',
        check_receipts(_r7, {}, bank, quiet=True) >= 1)

    # ⑧ 🧬 ใบเสร็จที่กวาดตอนคลังเล็กกว่า ⇒ ต้องแดง (กงล้อชั้น 2)
    # ⚠️ 8 ส.ค. 69 (ทาง ค): `PLAN` ว่างแล้ว ⇒ ถ้ายังส่ง PLAN เข้าไป เคสนี้จะ
    #    "เขียวเพราะไม่มีอะไรให้ตรวจ" ⛔ ไม่ใช่ "เขียวเพราะกงล้อทำงาน" (⑯)
    #    ⇒ ต้องประกอบแผนสมมติที่มี id จริงอยู่ข้างใน ไม่งั้นด่านนี้ตายเงียบ
    _keep = dict(RECEIPTS)
    _plan8 = {'q166': PLAN_ORPHANED['q166']}
    try:
        RECEIPTS['q166'] = ('collide_b22.py', '2026-08-08',
                            '63ไฟล์·%dข้อ·%s' % (bank['questions'] - 5, bank['idDigest']))
        _n8 = check_receipts(REG, _plan8, bank, quiet=True)
        _n8ctl = check_receipts(REG, _plan8, bank, quiet=True)
    finally:
        RECEIPTS.clear()
        RECEIPTS.update(_keep)
    _n8fresh = check_receipts(REG, _plan8, bank, quiet=True)
    say('⑧', '🧬 ใบเสร็จกวาดจากคลังเก่า ⇒ ต้องแดง', _n8 >= 1)
    #    ⑧ก คู่ควบคุม: ใบเสร็จตัวจริง (ป้ายตรง) บนแผนสมมติเดียวกัน ⇒ ต้องเขียว
    #    ⇒ พิสูจน์ว่า ⑧ แดงเพราะ "ป้ายเก่า" ⛔ ไม่ใช่เพราะแผนสมมติผิดรูป
    say('⑧ก', 'คู่ควบคุม: ป้ายตรง บนแผนเดียวกัน ⇒ ต้องเขียว', _n8fresh == 0)

    # ⑨ กงล้อ PRE_RECEIPT ต้องไม่โต และต้องพอดีกับ REG ที่มีอยู่จริง
    say('⑨', 'กงล้อ PRE_RECEIPT ⊆ REG และไม่โต',
        PRE_RECEIPT <= set(REG) and len(PRE_RECEIPT) <= PRE_RECEIPT_CEILING)

    # ⑩ 🧬 พิสูจน์ว่า "ชั้น 2+3 คือสิ่งที่จับ ⑥ ได้" ⛔ ไม่ใช่ชั้นแม่พิมพ์เดิม
    #    แม่พิมพ์ของ qNOSWEEP สะอาดสนิท ⇒ report() ต้องได้ 0
    #    ⇒ ถ้า verdict ยังแดง แปลว่าแดงเพราะใบเสร็จจริง ๆ
    _m10 = dict(REG)
    _m10['qNOSWEEP'] = _clean_mold
    say('⑩', '🧬 ชั้นแม่พิมพ์เงียบ แต่ verdict ยังแดง',
        report('x', _m10, quiet=True) == 0
        and verdict(REG, {'qNOSWEEP': _clean_mold}, quiet=True) >= 1)

    # ⑪ 🧬 ถ้าตัดชั้น 2+3 ออก ⇒ ⑥ ต้องหลุด (ด่านนี้รับน้ำหนักจริง ⛔ ไม่ใช่พิธีกรรม)
    say('⑪', '🧬 ตัดชั้น 2+3 ออก ⇒ ⑥ หลุดทันที',
        verdict(REG, {'qNOSWEEP': _clean_mold}, quiet=True, check_bank=False) == 0)

    # ═══ 🪧 แฟ้มกักกัน (ทาง ค · 8 ส.ค. 69) ═══
    _orph_mold = PLAN_ORPHANED['q172'] if 'q172' in PLAN_ORPHANED else None
    # ⑫ แม่พิมพ์ที่ตรงกับแถวในแฟ้มกักกัน ⇒ ต้อง **ปล่อย** (แฟ้มกักกันไม่มีน้ำหนัก)
    say('⑫', 'แม่พิมพ์ตรงแถวกักกัน ⇒ ต้องปล่อย',
        _orph_mold is not None
        and report('x', dict(REG, **{'qNEW': _orph_mold}), quiet=True) == 0)
    # ⑬ 🧬 ย้ายแถวเดียวกันกลับเข้า "แผน" ⇒ ต้องปฏิเสธทันที
    #    ⇒ ข้อพิสูจน์ว่า "การอยู่ในแฟ้มกักกัน" คือสิ่งที่ตัดน้ำหนัก ⛔ ไม่ใช่ความบังเอิญ
    say('⑬', '🧬 ย้ายกลับเข้าแผน ⇒ ต้องปฏิเสธทันที',
        _orph_mold is not None
        and report('x', dict(REG, **{'q172': _orph_mold, 'qNEW': _orph_mold}),
                   quiet=True) >= 1)
    # ⑭ ด่านเฝ้าแฟ้มกักกันเอง — ของจริงต้องสะอาด · ของล่อต้องแดง
    say('⑭', 'ด่านแฟ้มกักกัน: ของจริงสะอาด',
        check_quarantine(REG, PLAN, PLAN_ORPHANED, quiet=True) == 0)
    say('⑭ก', '🧬 อ้างแฟ้มกักกันเป็นของจริง (id ซ้ำใน PLAN) ⇒ ต้องแดง',
        check_quarantine(REG, {'q172': _orph_mold}, PLAN_ORPHANED, quiet=True) >= 1)
    say('⑭ข', '🧬 ลบแถวทิ้งทั้งแฟ้มแต่ใบเสร็จยังอยู่ ⇒ ต้องแดง',
        check_quarantine(REG, PLAN, {}, quiet=True) >= 1)
    return ok


if '--selftest' in sys.argv:
    print('▼▼▼ ชุดทดสอบของด่านเอง (㊶) ▼▼▼')
    passed = selftest()
    print('ผลชุดทดสอบ:', 'ผ่านครบ 17 ✅' if passed else 'ล้ม ❌')
    sys.exit(0 if passed else 1)

nfail = verdict(REG, PLAN)

if '--test' in sys.argv:
    print()
    print('▼▼▼ ชุดทดสอบของด่านเอง (㊶) ▼▼▼')
    if not selftest():
        nfail += 1

sys.exit(1 if nfail else 0)
