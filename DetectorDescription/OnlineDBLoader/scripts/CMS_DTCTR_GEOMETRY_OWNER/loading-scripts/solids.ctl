LOAD DATA
INFILE './data/SOLIDS.dat'
BADFILE './data/SOLIDS.bad'
DISCARDFILE './data/SOLIDS.dsc'
INSERT INTO TABLE CMSINTEGRATION.SOLIDS
FIELDS TERMINATED by ","
(
 ITEM_ID CHAR,
 SOL_TYPE CHAR
)
 