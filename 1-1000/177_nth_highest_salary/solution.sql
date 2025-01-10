CREATE
OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
RETURN QUERY(
    select
        case
            when N >= 1
            then (select distinct employee.salary
                from employee order by salary desc limit 1 offset N - 1)
            else null end
            as slr
  );
END;
$$
LANGUAGE plpgsql;