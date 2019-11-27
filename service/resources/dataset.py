from flask_restful import Resource
from flask import request, flash, redirect
from werkzeug.utils import secure_filename
import os, shutil

class Dataset(Resource):
    # 允许的文件后缀类型
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    UPLOAD_FOLDER = 'data'

    @staticmethod
    def allowed_file(filename):
        '''
            检查文件类型的合法性，目前只允许图片文件
        '''
        return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in Dataset.ALLOWED_EXTENSIONS

    def post(self, task_type, user_id, task_id):
        # 检查file是否在request中
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        # 获取文件对象
        file = request.files['file']

        # 如果用户没有选择文件，确点击了上传，那么浏览器还是会发送一个POST请求
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and Dataset.allowed_file(file.filename):
            directory = os.path.join(Dataset.UPLOAD_FOLDER, 
                                    task_type,
                                    user_id,
                                    task_id,
                                    os.path.split(request.form['relativePath'])[0])

        # 若文件夹不存在，递归地创建
        if not os.path.isdir(directory):
            os.makedirs(directory, exist_ok=True)

        filename = secure_filename(file.filename)
        file.save(os.path.join(directory, filename))
        return '''ok'''
        
