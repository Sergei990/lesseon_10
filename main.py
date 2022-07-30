from utilite import load_candidates, candidates

from flask import Flask


def main():
    fuck = load_candidates(candidates)

    app = Flask(__name__)

    #
    @app.route('/')
    def name_candidats():
        result = str()
        for candidates in range(len(fuck)) and fuck:
            result += f"\nИмя кандидата - {candidates['name']}\n"
            result += f"Позиция кандидата - {candidates['position']}\n"
            result += f"Навыки через запятую - {candidates['skills']}\n"
        return f'<pre> {result}</pre>'

    @app.route('/candidates/<int:x>')
    def pk_candidat(x):

        for pk_candidate in fuck:
            photo = pk_candidate["picture"]
            if pk_candidate['pk'] == x:
                return f"<img src = '{photo}'>" \
                       f"<pre>\nИмя кандидата - {pk_candidate['name']}\n" \
                       f"Позиция кандидата - {pk_candidate['position']}\n" \
                       f"Навыки через запятую - {pk_candidate['skills']}\n</pre>"
        return f"Нет такого кандидата (((("

    @app.route('/skills/<x>')
    def get_by_skill(x):

        candidate = str()
        user = str(x).lower()

        for skills_candidate in fuck:

            if user in str(skills_candidate['skills']).lower():
                candidate += (f"\nИмя кандидата - {skills_candidate['name']}\n")
                candidate += (f"Позиция кандидата - {skills_candidate['position']}\n")
                candidate += (f"Навыки через запятую - {''.join(skills_candidate['skills'])}\n")

        return f"<pre> {candidate} </pre>"

    app.run()


if __name__ == '__main__':
    main()
