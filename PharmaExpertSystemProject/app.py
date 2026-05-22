from flask import Flask, render_template, request

app = Flask(__name__)

# Disease to medicine mapping

disease_medicine_map = {
    "fever": "Paracetamol 500mg",
    "headache": "Disprin",
    "cold": "Cetrizine",
    "cough": "Benadryl Syrup",
    "flu": "Tamiflu",
    "body pain": "Ibuprofen",
    "sore throat": "Strepsils",
    "nausea": "Domperidone",
    "diarrhea": "Loperamide",
    "constipation": "Lactulose",
    "hypertension": "Amlodipine",
    "diabetes": "Metformin",
    "high cholesterol": "Atorvastatin",
    "asthma": "Salbutamol Inhaler",
    "allergy": "Loratadine",
    "insomnia": "Zolpidem",
    "anxiety": "Alprazolam",
    "depression": "Fluoxetine",
    "arthritis": "Naproxen",
    "migraine": "Sumatriptan",
    "sinusitis": "Amoxicillin",
    "acne": "Benzoyl Peroxide",
    "eczema": "Hydrocortisone Cream",
    "psoriasis": "Calcipotriol",
    "anemia": "Ferrous Sulfate",
    "thyroid": "Levothyroxine",
    "gastritis": "Pantoprazole",
    "acid reflux": "Omeprazole",
    "heartburn": "Ranitidine",
    "UTI": "Nitrofurantoin",
    "kidney stones": "Tamsulosin",
    "gout": "Allopurinol",
    "hepatitis B": "Tenofovir",
    "hepatitis C": "Sofosbuvir",
    "malaria": "Artemether-Lumefantrine",
    "tuberculosis": "Isoniazid",
    "pneumonia": "Azithromycin",
    "bronchitis": "Clarithromycin",
    "tonsillitis": "Penicillin",
    "eye infection": "Tobramycin Eye Drops",
    "ear infection": "Ofloxacin Ear Drops",
    "dizziness": "Meclizine",
    "vertigo": "Betahistine",
    "joint pain": "Diclofenac",
    "back pain": "Etoricoxib",
    "toothache": "Paracetamol + Clindamycin",
    "mouth ulcer": "Choline Salicylate Gel",
    "bleeding gums": "Chlorhexidine Mouthwash",
    "bad breath": "Zinc Mouth Rinse",
    "obesity": "Orlistat",
    "vitamin D deficiency": "Cholecalciferol",
    "calcium deficiency": "Calcium Carbonate",
    "low B12": "Methylcobalamin",
    "scabies": "Permethrin Cream",
    "lice": "Malathion Lotion",
    "ringworm": "Clotrimazole Cream",
    "fungal infection": "Fluconazole",
    "bacterial infection": "Ciprofloxacin",
    "viral infection": "Acyclovir",
    "chickenpox": "Calamine Lotion",
    "measles": "Paracetamol + Rest",
    "mumps": "Ibuprofen + Cold Compress",
    "rubella": "Paracetamol + Fluids",
    "conjunctivitis": "Chloramphenicol Eye Drops",
    "pink eye": "Artificial Tears",
    "dry eyes": "Carboxymethylcellulose Eye Drops",
    "glaucoma": "Timolol Eye Drops",
    "cataract": "Surgery Recommendation",
    "prostatitis": "Levofloxacin",
    "enlarged prostate": "Finasteride",
    "impotence": "Sildenafil",
    "menstrual pain": "Mefenamic Acid",
    "PCOS": "Metformin + OCPs",
    "menopause": "HRT",
    "breast pain": "Evening Primrose Oil",
    "pregnancy vomiting": "Doxylamine + Pyridoxine",
    "motion sickness": "Dimenhydrinate",
    "travel diarrhea": "Rifaximin",
    "food poisoning": "ORS + Ciprofloxacin",
    "dehydration": "ORS Solution",
    "burn": "Silver Sulfadiazine Cream",
    "wound infection": "Mupirocin",
    "skin allergy": "Cetirizine",
    "insect bite": "Hydrocortisone",
    "bee sting": "Antihistamine + Ice Pack",
    "fracture pain": "Tramadol",
    "sprain": "Aceclofenac",
    "fatigue": "Vitamin B Complex",
    "weakness": "Multivitamins",
    "memory loss": "Ginkgo Biloba",
    "low immunity": "Zinc + Vitamin C",
    "hair loss": "Minoxidil",
    "dandruff": "Ketoconazole Shampoo",
    "itchy scalp": "Coal Tar Shampoo",
    "sunburn": "Aloe Vera Gel",
    "dark spots": "Vitamin C Serum",
    "wrinkles": "Retinoid Cream",
    "high uric acid": "Febuxostat",
    "low blood pressure": "Fludrocortisone",
    "panic attack": "Clonazepam",
    "schizophrenia": "Olanzapine",
    "bipolar disorder": "Lithium Carbonate",
    "autism": "Therapy Referral",
    "ADHD": "Methylphenidate",
    "Parkinson’s": "Levodopa + Carbidopa",
    "Alzheimer’s": "Donepezil"
}
    # Add more if needed


@app.route("/", methods=["GET", "POST"])
def index():
    recommended_medicines = []
    if request.method == "POST":
        diseases = request.form.getlist("disease")
        for d in diseases:
            d_clean = d.lower().strip()
            if d_clean in disease_medicine_map:
                recommended_medicines.append((d, disease_medicine_map[d_clean]))
            else:
                recommended_medicines.append((d, "No recommendation found."))
    return render_template("index.html", medicines=recommended_medicines)

if __name__ == "__main__":
    app.run(debug=True)
