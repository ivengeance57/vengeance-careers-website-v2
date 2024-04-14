from flask import Flask, json, jsonify, render_template

from database import load_jobs_from_db

app = Flask(__name__)


@app.route("/")
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs, company_name='Vengeance')


@app.route("/api/jobs")
def list_jobs():
  job_list = load_jobs_from_db()
  return jsonify(job_list)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
