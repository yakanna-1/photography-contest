from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data to store participants, photos, and ratings (you can use a database later)
participants = []
photos = []
ratings = {}

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# Submit photo route
@app.route('/submit_photo', methods=['GET', 'POST'])
def submit_photo():
    if request.method == 'POST':
        # Collect participant details and photo submission
        name = request.form['name']
        email = request.form['email']
        title = request.form['title']
        description = request.form['description']
        photo = request.form['photo']  # This could be an uploaded file, but here it's just a text input

        participant = {'name': name, 'email': email}
        photo_data = {'title': title, 'description': description, 'photo': photo}

        participants.append(participant)
        photos.append(photo_data)

        return redirect(url_for('home'))
    return render_template('submit_photo.html')

# Rate photos route (for judges only)
@app.route('/rate_photos', methods=['GET', 'POST'])
def rate_photos():
    if request.method == 'POST':
        judge_name = request.form['judge_name']
        for photo in photos:
            score = int(request.form[f'score_{photo["title"]}'])
            if photo["title"] not in ratings:
                ratings[photo["title"]] = []
            ratings[photo["title"]].append({'judge': judge_name, 'score': score})

        return redirect(url_for('home'))
    return render_template('rate_photos.html', photos=photos)

# View results route
@app.route('/results')
def results():
    photo_scores = {}
    for title, scores in ratings.items():
        avg_score = sum([score['score'] for score in scores]) / len(scores)
        photo_scores[title] = avg_score

    sorted_photos = sorted(photo_scores.items(), key=lambda x: x[1], reverse=True)
    return render_template('results.html', sorted_photos=sorted_photos)

if __name__ == '__main__':
    app.run(debug=True)
