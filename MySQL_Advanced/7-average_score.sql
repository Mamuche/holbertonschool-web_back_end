-- script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. Note: An average score can be a decimal
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE av_score FLOAT;

    SELECT AVG(score)
    -- fonction qui sert à calculer la moyenne des valeurs dans une colonne(score)
    INTO av_score
    FROM corrections
    WHERE corrections.user_id = user_id;

    UPDATE users
    SET average_score = av_score
    WHERE id = user_id;
END;
$$

DELIMITER ;
