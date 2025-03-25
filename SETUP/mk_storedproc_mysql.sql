use presidents;
DELIMITER //
CREATE PROCEDURE pres_full_name
(IN term_num int)
BEGIN
  select concat(fname, ' ', lname)
  from presidents
  where num = term_num;
END //
DELIMITER ;
