from flask import Flask, render_template, request, redirect
import data_handler

app = Flask(__name__)


@app.route('/list')
@app.route('/')
def initial_data():
    file_data = data_handler.get_all_user_story()
    return render_template('list.html', data=file_data)


@app.route('/story', methods=["GET", "POST"])
def add_new():
    new_id = data_handler.generate_id()
    if request.method == 'POST':
        user_story = {
            "id": new_id,
            "title": request.form.get('title'),
            "user_story": request.form.get('user_story'),
            "acceptance_criteria": request.form.get('acceptance_criteria'),
            "business_value": request.form.get('business_value'),
            "estimation": request.form.get('estimation')}
        data_handler.add_on_csv(user_story)
        return redirect('/')
    return render_template('story.html')


@app.route('/story/<id>', methods=["GET", "POST"])
def update(id):
    if request.method == 'GET':
        file_data = data_handler.get_all_user_story(id)

    if request.method == 'POST':
        user_story = {
            "id": id,
            "title": request.form.get('title'),
            "user_story": request.form.get('user_story'),
            "acceptance_criteria": request.form.get('acceptance_criteria'),
            "business_value": request.form.get('business_value'),
            "estimation": request.form.get('estimation'),
            "status": request.form.get('status')}
        data_handler.update_on_csv(id, user_story)
        return redirect('/')
    return render_template('update.html', id=id, data=file_data)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
