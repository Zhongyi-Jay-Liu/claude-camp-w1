DISCLAIMER = ("⚠  BMI applies to adults 18–65 only. NOT suitable for: children/teens "
              "(use CDC growth charts), pregnant women, elderly 65+, or athletes.")
BANDS = [(18.5,"Underweight","Consult a dietitian; focus on nutrient-dense foods."),
         (25.0,"Normal weight","Great! Keep up balanced eating and regular exercise."),
         (30.0,"Overweight","Diet + activity changes can help; see your GP if unsure."),
         (35.0,"Obese Class I","Speak with a healthcare provider for a tailored plan."),
         (40.0,"Obese Class II","Medical guidance is strongly recommended."),
         (float("inf"),"Obese Class III","Please seek urgent medical support.")]

def get_float(prompt):
    while True:
        try:
            v = float(input(prompt))
            if v > 0: return v
            raise ValueError
        except ValueError:
            print("  ✗ Enter a positive number.")

def get_unit(label, opts):
    while (u := input(f"{label} unit ({'/'.join(opts)}): ").strip().lower()) not in opts:
        print(f"  ✗ Choose: {'/'.join(opts)}")
    return u

w = get_float("Weight: ")
kg = w * (0.453592 if get_unit("Weight", ["kg","lb"]) == "lb" else 1)
h = get_float("Height: ")
m  = h * (0.0254   if get_unit("Height", ["cm","in"]) == "in"  else 0.01)

bmi = kg / m ** 2
_, cat, tip = next(b for b in BANDS if bmi < b[0])
print(f"\n  BMI: {bmi:.1f} — {cat}\n  {tip}\n\n{DISCLAIMER}")
