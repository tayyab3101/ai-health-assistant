print("=== AI Smart Health Assistant ===")

# =========================
# USER INPUT
# =========================
name = input("Enter your name: ")
gender = input("Enter your gender (Male/Female): ")
age = int(input("Enter your age: "))
height = float(input("Enter your height (in meters): "))
weight = float(input("Enter your weight (in kg): "))
goal = input("Enter your goal (lose/gain/maintain): ")
allergy = input("Enter any food you want to avoid (or press Enter to skip): ")

# =========================
# BMI CALCULATION
# =========================
bmi = weight / (height ** 2)

print("\n===== USER REPORT =====")
print("Name:", name)
print("Gender:", gender)
print("Age:", age)
print("BMI:", round(bmi, 2))

# =========================
# AI DECISION MODULE
# =========================
print("\n===== AI ANALYSIS =====")

if bmi < 18.5:
    print("Category: Underweight")
    print("AI Suggestion: You should gain weight 💪")

elif bmi >= 18.5 and bmi < 25:
    print("Category: Normal")
    print("AI Suggestion: Maintain your health 👍")

else:
    print("Category: Overweight")
    print("AI Suggestion: You should lose weight 🏃")

# =========================
# DIET PLAN MODULE
# =========================
print("\n===== DIET PLAN =====")

breakfast = []
lunch = []
dinner = []

# Goal-based diet
if goal.lower() == "gain":
    breakfast = ["Eggs", "Peanut Butter", "Milk"]
    lunch = ["Rice", "Chicken", "Potatoes"]
    dinner = ["Meat", "Bread", "Yogurt"]

elif goal.lower() == "lose":
    breakfast = ["Green Tea", "Fruits"]
    lunch = ["Grilled Chicken", "Salad"]
    dinner = ["Soup", "Vegetables"]

else:
    breakfast = ["Oats", "Fruits", "Milk"]
    lunch = ["Rice", "Vegetables", "Chicken"]
    dinner = ["Salad", "Soup", "Bread"]

# =========================
# ALLERGY FILTER MODULE
# =========================
if allergy:
    allergy = allergy.lower()

    breakfast = [item for item in breakfast if allergy not in item.lower()]
    lunch = [item for item in lunch if allergy not in item.lower()]
    dinner = [item for item in dinner if allergy not in item.lower()]

    print(f"\nNote: '{allergy}' removed from your diet plan ❌")

# =========================
# FINAL OUTPUT
# =========================
print("\n--- FINAL DIET PLAN ---")
print("Breakfast:", ", ".join(breakfast))
print("Lunch:", ", ".join(lunch))
print("Dinner:", ", ".join(dinner))

print("\n=== THANK YOU FOR USING AI HEALTH ASSISTANT ===")