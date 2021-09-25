CREATE OR REPLACE STREAM "RAW_ANAMOLIES" ("favoritecaptain" varchar(32), "rating" INTEGER, "ANOMALY_SCORE" DOUBLE);
CREATE OR REPLACE PUMP "RAW_PUMP" AS
INSERT INTO "RAW_ANAMOLIES"
SELECT "favoritecaptain", "rating", "ANOMALY_SCORE"
FROM TABLE(
    RANDOM_CUT_FOREST(CURSOR(SELECT STREAM "favoritecaptain", "rating" FROM "SOURCE_SQL_STREAM_001"))
);

CREATE OR REPLACE STREAM "ORDERED_ANAMOLIES" ("favoritecaptain" varchar(32), "rating" INTEGER, "ANOMALY_SCORE" DOUBLE);

CREATE OR REPLACE PUMP "ORDERED_PUMP" AS
INSERT INTO "ORDERED_ANAMOLIES"
SELECT STREAM *
FROM "RAW_ANAMOLIES"
ORDER BY FLOOR("RAW_ANAMOLIES".ROWTIME TO SECOND), "ANOMALY_SCORE" desc;
