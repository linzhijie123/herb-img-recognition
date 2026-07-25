# app.py
from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
app.secret_key = 'your-secret-key-here'

# 确保上传目录存在
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # 检查是否有文件被上传
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('4.html', filename=filename)

    return render_template('4.html')


if __name__ == '__main__':
    app.run(debug=True)






# model.train()
# # 配置loss函数
# cross_entropy = paddle.nn.CrossEntropyLoss()
# # 配置参数优化器
# optimizer = paddle.optimizer.Adam(learning_rate=0.0001,
#                                   parameters=model.parameters())
#
# steps = 0
# train_loss, train_acc,val_loss,val_acc = [], [], [],[]
