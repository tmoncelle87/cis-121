from tkinter.tix import INTEGER


human_age= float(input("what is your age?"))
dog_age= human_age * 7
dog_age_in_years=int(dog_age)
dog_age_in_months=int((dog_age-dog_age_in_years)*12)
dog_age_in_days=int((dog_age-dog_age_in_years+dog_age_in_months))*60
print("A dog should be",dog_age_in_years,"years old and should be",dog_age_in_months,"months old and should be",dog_age_in_days,"days old")

human_ages= float(input("what is your age?"))
cat_age= human_ages * 9 
cat_age_in_years=int(cat_age)
cat_age_in_months=int((cat_age-cat_age_in_years)*12)
cat_age_in_days=int((cat_age-cat_age_in_years+cat_age_in_months))*60
print("A cat should be",cat_age_in_years,"years old and should be",cat_age_in_months,"months old and should be",cat_age_in_days,"days old")

human_agess = float(input("what is your age?"))
horse_years = 3 * ((((human_age**2-47)/7))+12)
horse_age_in_years=int(horse_years)
Horse_age_in_months=int((horse_years-horse_age_in_years)*12)
print("an age", human_agess,"human should be about",horse_years,"in horse age")
horse_age_in_days=int((horse_years-horse_age_in_years+Horse_age_in_months))*60
print("A horse should be",horse_age_in_years,"years old and should be",Horse_age_in_months,"months old and should be",horse_age_in_days,"days old")
