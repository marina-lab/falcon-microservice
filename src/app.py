import falcon
import json
import os
import psycopg2
import psycopg2.extras

DB_CONN_URI = os.environ['DATABASE_URL']

def get_cursor():
    """Get a connection/cursor"""
    conn = psycopg2.connect(DB_CONN_URI)
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    return cur

def fetch_things(cur):
    cur.execute('SELECT * FROM things')
    return [dict(t) for t in cur.fetchall()]

class ThingsResource:
    def on_get(self, req, resp):
        """Get the things from the database and return as JSON."""

        cur = get_cursor()
        things = fetch_things(cur)

        things_dict = {'things': things}

        things_json = json.dumps(things_dict)

        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = things_json

app = falcon.API()

things = ThingsResource()

app.add_route('/things', things)
