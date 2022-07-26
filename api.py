from urllib import response
from posts import *

#gets all posts
@app.route("/posts", methods=["GET"])
def get_posts():
    return jsonify({"Posts": Posts.get_all_posts()})

#gets post with specific id
@app.route("/posts/<int:id>", methods=["GET"])
def get_posts_by_id(id):
    return_value = Posts.get_post(id)
    return jsonify(return_value)

#post new post
@app.route("/posts", methods=["POST"])
def add_post():
    request_data = request.get_json()
    Posts.add_post(request_data["title"], request_data["genre"])
    response = Response("Post added", 201, mimetype="application/json")
    return response

#update post with a specific id
@app.route("/posts/<int:id>", methods=["PUT"])
def update_post():
    request_data = request.get_json()
    Posts.update_post(id, request_data["title"], request_data["genre"])
    response = Response("Post Updated", 200, mimetype="application/json")
    return response

#delete specified post by id
@app.route("/posts/<int:id>", methods=["DELETE"])
def remove_post():
    Posts.delete_post(id)
    response = Response("Post Deleted", 200, mimetype="application/json")
    return response


if __name__ == "__main__":
    app.run(port=1234, debug=False)
