from flask import Flask, render_template, request
import math

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    ans = 'Введите данные'

    v1 = ''
    v2 = ''
    pr = '2'
    sh = 'sphere'

    if request.method == 'POST':

        sh = request.form.get('shape', 'sphere')
        v1 = request.form.get('val1', '')
        v2 = request.form.get('val2', '')
        pr = request.form.get('precision', '2')

        try:
            a = float(v1)
            p = int(pr)

            if a <= 0:
                ans = 'Ошибка: число должно быть больше 0'

            else:

                if sh == 'sphere':
                    res = (4 / 3) * math.pi * a ** 3

                elif sh == 'cube':
                    res = a ** 3

                else:
                    h = float(v2)

                    if h <= 0:
                        ans = 'Ошибка: высота должна быть больше 0'
                        return render_template(
                            'index.html',
                            ans=ans,
                            v1=v1,
                            v2=v2,
                            pr=pr,
                            sh=sh
                        )

                    if sh == 'cylinder':
                        res = math.pi * a ** 2 * h

                    elif sh == 'cone':
                        res = (1 / 3) * math.pi * a ** 2 * h

                    elif sh == 'pyramid':
                        res = (1 / 3) * a ** 2 * h

                    else:
                        res = 0

                ans = f'Результат: {res:.{p}f}'

        except ValueError:
            ans = 'Ошибка ввода!'

    return render_template(
        'index.html',
        ans=ans,
        v1=v1,
        v2=v2,
        pr=pr,
        sh=sh
    )


if __name__ == '__main__':
    app.run(debug=True)