import file_operations
from faker import Faker
import random
import os


def main():
    path = "result"
    os.makedirs(path, exist_ok=True)

    fake = Faker("ru_RU")

    skill1 = "Ледяной удар"
    skill2 = "Кислотный взгляд"
    skill3 = "Стремительный прыжок"
    skill4 = "Электрический выстрел"
    skill5 = "Огненный заряд"
    skill6 = "Тайный побег"
    skill7 = "Стремительный удар"

    letters_mapping = {
        'а': 'а͠',
        'б': 'б̋',
        'в': 'в͒͠',
        'г': 'г͒͠',
        'д': 'д̋',
        'е': 'е͠',
        'ё': 'ё͒͠',
        'ж': 'ж͒',
        'з': 'з̋̋͠',
        'и': 'и',
        'й': 'й͒͠',
        'к': 'к̋̋',
        'л': 'л̋͠',
        'м': 'м͒͠',
        'н': 'н͒',
        'о': 'о̋',
        'п': 'п̋͠',
        'р': 'р̋͠',
        'с': 'с͒',
        'т': 'т͒',
        'у': 'у͒͠',
        'ф': 'ф̋̋͠',
        'х': 'х͒͠',
        'ц': 'ц̋',
        'ч': 'ч̋͠',
        'ш': 'ш͒͠',
        'щ': 'щ̋',
        'ъ': 'ъ̋͠',
        'ы': 'ы̋͠',
        'ь': 'ь̋',
        'э': 'э͒͠͠',
        'ю': 'ю̋͠',
        'я': 'я̋',
        'А': 'А͠',
        'Б': 'Б̋',
        'В': 'В͒͠',
        'Г': 'Г͒͠',
        'Д': 'Д̋',
        'Е': 'Е',
        'Ё': 'Ё͒͠',
        'Ж': 'Ж͒',
        'З': 'З̋̋͠',
        'И': 'И',
        'Й': 'Й͒͠',
        'К': 'К̋̋',
        'Л': 'Л̋͠',
        'М': 'М͒͠',
        'Н': 'Н͒',
        'О': 'О̋',
        'П': 'П̋͠',
        'Р': 'Р̋͠',
        'С': 'С͒',
        'Т': 'Т͒',
        'У': 'У͒͠',
        'Ф': 'Ф̋̋͠',
        'Х': 'Х͒͠',
        'Ц': 'Ц̋',
        'Ч': 'Ч̋͠',
        'Ш': 'Ш͒͠',
        'Щ': 'Щ̋',
        'Ъ': 'Ъ̋͠',
        'Ы': 'Ы̋͠',
        'Ь': 'Ь̋',
        'Э': 'Э͒͠͠',
        'Ю': 'Ю̋͠',
        'Я': 'Я̋',
        '': ''
    }

    for original, letters_mapping in letters_mapping.items():
        skill1 = skill1.replace(original, letters_mapping)
        skill2 = skill2.replace(original, letters_mapping)
        skill3 = skill3.replace(original, letters_mapping)
        skill4 = skill4.replace(original, letters_mapping)
        skill5 = skill5.replace(original, letters_mapping)
        skill6 = skill6.replace(original, letters_mapping)
        skill7 = skill7.replace(original, letters_mapping)

    runic_skills = []
    runic_skills.append(skill1)
    runic_skills.append(skill2)
    runic_skills.append(skill3)
    runic_skills.append(skill4)
    runic_skills.append(skill5)
    runic_skills.append(skill6)
    runic_skills.append(skill7)

    for skill in runic_skills:
        skill_1 = random.choice(runic_skills)
        skill_2 = random.choice(runic_skills)
        skill_3 = random.choice(runic_skills)
        selected_skills = random.sample(runic_skills, 3)
        skill_1, skill_2, skill_3 = selected_skills

    charsheets = []
    for i in range(10):
        context = {
            "first_name": fake.first_name_female(),
            "last_name": fake.last_name(),
            "job": fake.job(),
            "town": fake.city(),
            "strength": random.randint(3, 18),
            "agility": random.randint(3, 18),
            "endurance": random.randint(3, 18),
            "intelligence": random.randint(3, 18),
            "luck": random.randint(3, 18),
            "skill_1": skill_1,
            "skill_2": skill_2,
            "skill_3": skill_3,
        }
        character = {"id": i+1, "context": context}
        charsheets.append(character)
        file_name = "result_{}.svg".format(i+1)
        file_operations.render_template("charsheet.svg", os.path.join(path, file_name), context)


if __name__ == '__main__':
    main()
