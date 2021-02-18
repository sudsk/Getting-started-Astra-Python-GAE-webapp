from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import dict_factory
from cassandra.query import named_tuple_factory
from cassandra.query import SimpleStatement
import uuid, binascii, os

cloud_config= {
        'secure_connect_bundle': 'secure-connect-killrvideocluster.zip',
        'use_default_tempdir': True
}
auth_provider = PlainTextAuthProvider(os.environ.get('ASTRAUSER'), os.environ.get('ASTRAPASSWORD'))
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect("killrvideo")
session.row_factory = dict_factory

def read(id):
    main_dict = session.execute("SELECT isbn as id, title, author, published_date, description, image_url FROM books_by_isbn WHERE isbn = %s",[id]).one()
    return main_dict

def delete(id):
    result = session.execute("SELECT published_date, category FROM books_by_isbn WHERE isbn = %s", [id]).one()
    session.execute("DELETE FROM books_by_isbn WHERE isbn = %s",[id])
    session.execute("DELETE FROM books_by_category WHERE category = %s AND published_date = %s AND isbn = %s",[result['category'], result['published_date'], id])

def create(data):
    session.execute('INSERT INTO books_by_isbn (isbn, title, author, category, published_date,description, image_url) VALUES (%s, %s, %s, %s, %s, %s, %s)', \
                      [data['isbn'], data['title'], data['author'], data['category'], data['published_date'], data['description'], data['image_url']])
    session.execute('INSERT INTO books_by_category (isbn,title,author,category,published_date,description, image_url) VALUES (%s, %s, %s, %s, %s, %s, %s)', \
                      [data['isbn'], data['title'], data['author'], data['category'], data['published_date'], data['description'], data['image_url']])
    return data['isbn']

def update(data, id):
    result = session.execute("SELECT published_date, category FROM books_by_isbn WHERE isbn = %s", [id]).one()
    session.execute("UPDATE books_by_isbn SET title = %s, author = %s, description = %s WHERE isbn = %s",[data['title'],data['author'],data['description'],id])
    session.execute("UPDATE books_by_category SET title=%s,author=%s,description=%s WHERE category = %s AND published_date = %s AND isbn = %s", [data['title'], data['author'], data['description'], result['category'], result['published_date'], id])
    return id

def next_page(limit=20, ps=None):
    if ps is not None:
        paging_state = bytes.fromhex(ps)
    else:
        paging_state = ps
    
    query = "SELECT isbn as id, title, author, published_date, description, image_url FROM books_by_category WHERE category = 'Food-Drink'"
    statement = SimpleStatement(query, fetch_size=limit)
    docs = session.execute(statement, paging_state=paging_state)

    # save the paging_state somewhere and return current results
    if docs.paging_state is not None:
        new_ps = docs.paging_state.hex()
    else:
        new_ps = None
    
    return docs, new_ps
