-- Create a stored procedure to compute the average score
-- for a user and update the average_score column in the users table.
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser (
    IN user_id_param INT
)
BEGIN
    DECLARE user_avg_score FLOAT;
    
    -- Calculate average score for the user
    SELECT AVG(score) INTO user_avg_score
    FROM corrections
    WHERE user_id = user_id_param;
    
    -- Update the average_score column in the users table
    UPDATE users
    SET average_score = user_avg_score
    WHERE id = user_id_param;
END //

<<<<<<< HEAD
DELIMITER ;
=======
DELIMITER ;
>>>>>>> d01a612edafbcb20b156d4f8e219d7deae1f7d56
