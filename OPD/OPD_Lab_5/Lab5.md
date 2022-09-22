```asm
ORG	0x35F
AMOUNT:	WORD	0000
ADDR:	WORD	$WORDS
RESULT:	WORD	0000
START:	CLA
	PUSH	
	CALL	FORIN
	POP		
	ST	AMOUNT
	ST	(ADDR)+
	BEQ	FINAL
FIRST:	PUSH
	CALL	FORIN
	POP
	SWAB
	ST	RESULT
	LD 	AMOUNT
	DEC
	CMP	#0
	BNE	CONTINUE
EXIT:	LD	RESULT
	ST	(ADDR)
	HLT
CONTINUE:	ST	AMOUNT
SECOND:	LD	RESULT
	PUSH
	CALL	FORIN
	POP
	ST	(ADDR)+
CHECK:	LD	AMOUNT
	DEC
	CMP	#0
	BNE	GOON
	HLT
GOON:	ST	AMOUNT
	CLA
	BR	FIRST
ORG	0x385
FORIN:	IN	5
	AND	#0x40
	BEQ	FORIN
	LD	&1
	IN	4
	ST	&1
	RET
FINAL:	HLT
ORG	0x612
WORDS:
```