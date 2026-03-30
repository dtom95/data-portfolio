-- ============================================
-- Youth Program Data Analysis
-- ============================================

-- 1. View dataset
SELECT * FROM outcomes;

-- 2. Average improvement across all participants
SELECT 
    AVG(Post_Score - Pre_Score) AS Avg_Improvement
FROM outcomes;

-- 3. Improvement by risk level
SELECT 
    Risk_Level,
    AVG(Post_Score - Pre_Score) AS Avg_Improvement
FROM outcomes
GROUP BY Risk_Level
ORDER BY Avg_Improvement DESC;

-- 4. Top 5 most improved participants
SELECT 
    Participant_ID,
    (Post_Score - Pre_Score) AS Improvement
FROM outcomes
ORDER BY Improvement DESC
LIMIT 5;

-- 5. Retention analysis (follow-up vs post)
SELECT 
    AVG(Follow_Up_Score - Post_Score) AS Retention_Change
FROM outcomes;