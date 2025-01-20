#pip install graphene
#pip install graphene-sqlalchemy

import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos SQLAlchemy
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)

    title = Column(String, nullable=False)
    author = Column(String, nullable=False)

# Crear la base de datos en memoria (puedes usar una base de datos real)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Insertar algunos datos de ejemplo en la base de datos
book1 = Book(title="1984", author="George Orwell")
book2 = Book(title="To Kill a Mockingbird", author="Harper Lee")
session.add(book1)
session.add(book2)
session.commit()

# Definición de los tipos de Graphene usando SQLAlchemyObjectType
class BookType(SQLAlchemyObjectType):
    class Meta:
        model = Book
        interfaces = (graphene.relay.Node, )

# Definición de las consultas
class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_books = SQLAlchemyConnectionField(BookType.connection)
    book_by_id = graphene.Field(BookType, id=graphene.Int())

    def resolve_book_by_id(self, info, id):
        return session.query(Book).filter(Book.id == id).first()

# Definición de las mutaciones
class CreateBook(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        author = graphene.String()

    book = graphene.Field(BookType)

    def mutate(self, info, title, author):
        book = Book(title=title, author=author)
        session.add(book)
        session.commit()
        return CreateBook(book=book)

class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()

# Esquema GraphQL
schema = graphene.Schema(query=Query, mutation=Mutation)

# Consultas de ejemplo
query_string = """
    query {
        allBooks {
            edges {
                node {
                    id
                    title
                    author
                }
            }
        }
    }
"""

# Ejecutar una consulta
result = schema.execute(query_string)
print(result.data['allBooks'])

# Mutación para crear un nuevo libro
mutation_string = """
    mutation {
        createBook(title: "Brave New World", author: "Aldous Huxley") {
            book {
                id
                title
                author
            }
        }
    }
"""

# Ejecutar la mutación
mutation_result = schema.execute(mutation_string)
print(mutation_result.data['createBook']['book'])
