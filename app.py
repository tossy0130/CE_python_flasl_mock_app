from flask import Flask, render_template, request, url_for, redirect
import os

app = Flask(__name__)


@app.route('/upload', methods=['GET', 'POST'])
def upload():

    # form submit 前　の画面表示
    if request.method == 'GET':
        return render_template('upload.html')

    # form で submit されたら
    elif request.method == 'POST':

        # === 画像保存処理 ===
        file = request.files['up_file']
        file.save(os.path.join('./static/image', file.filename))
        # === 画像保存処理 END ===

        # 【 案 １ 】 　
        # ================== CE のコードをここに記述して、
        # === 画像に CEC コードを付与して、下の uploaded_file 関数に渡す。
        # uploaded_file 関数の uploaded_file.html で CE の証明書発行 UI を作成する。

        return redirect(url_for('uploaded_file', filename=file.filename))


@app.route('/uploaded_file/<string:filename>')
def uploaded_file(filename):
    return render_template('uploaded_file.html', filename=filename)


if __name__ == '__main__':
    app.run(debug=True)
