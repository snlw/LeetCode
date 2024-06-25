-- https://leetcode.com/problems/invalid-tweets/submissions/1299654519
SELECT tweet_id 
FROM Tweets
WHERE LENGTH(content) > 15
