import pets_db

################################################################################
#     ____                          __     _                          __ __
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          / // /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \        / // /_
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /       /__  __/
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/          /_/   
#                                                                          
#  Question 4
################################################################################
#
# Instructions:
# Question 4 and Question 5 are about writing SQL. THey use the database that is 
# created in the file `pets_db.py`. 
# These questions use a database called SQLite. You do not need to install anything.
# In the file `pets_db.py` three tables are created. Data is then added to each 
# of the tables. The questions below are about how the data in each of the tables
# is related.

# Part 4.A:
# Write SQL to select the pets that are owned by nobody.
# The output should be a list of tuples in the format: (<pet name>, <species>, <age>)

sql_pets_owned_by_nobody = """
    SELECT NAME, SPECIES, AGE 
    FROM ANIMALS 
    LEFT JOIN PEOPLE_ANIMALS ON ANIMALS.ANIMAL_ID = PEOPLE_ANIMALS.PET_ID 
    WHERE PEOPLE_ANIMALS.PET_ID IS NULL
    """


# Part 4.B:
# Write SQL to select how the number of pets are older than their owners. 
# The output should be an integer.

sql_pets_older_than_owner = """
    SELECT COUNT(*) 
    FROM ANIMALS 
    JOIN PEOPLE_ANIMALS ON ANIMALS.ANIMAL_ID = PEOPLE_ANIMALS.PET_ID 
    JOIN PEOPLE ON PEOPLE_ANIMALS.OWNER_ID = PEOPLE.PERSON_ID 
    WHERE ANIMALS.AGE > PEOPLE.AGE
    """

# Part 4.C: BONUS CHALLENGE! 
# Write SQL to select the pets that are owned by Bessie and nobody else.
# The output should be a list of tuples in the format: (<person name>, <pet name>, <species>)

sql_only_owned_by_bessie = """
    SELECT PEOPLE.NAME AS PERSON_NAME, ANIMALS.NAME AS PET_ANIMAL, ANIMALS.SPECIES AS SPECIES 
    FROM ANIMALS 
    JOIN PEOPLE_ANIMALS ON ANIMALS.ANIMAL_ID = PEOPLE_ANIMALS.PET_ID 
    JOIN PEOPLE ON PEOPLE_ANIMALS.OWNER_ID = PEOPLE.PERSON_ID 
    WHERE PEOPLE.NAME = 'bessie' 
    AND PET_ID IN(SELECT PET_ID FROM PEOPLE_ANIMALS GROUP BY PET_ID HAVING COUNT(*) = 1) 
    GROUP BY PEOPLE.NAME,ANIMALS.NAME, ANIMALS.SPECIES 
    """