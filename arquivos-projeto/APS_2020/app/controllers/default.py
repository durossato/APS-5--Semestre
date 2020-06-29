from app import app, db
from flask import render_template,redirect,url_for, request
from app.models.forms import ExtrairForm
from app.models.tables import Noticia
from app.controllers.scrapping import scrap
from app.controllers.scrapping import linkVet, tituloVet, dataVet

a = ""

@app.route("/")
@app.route("/extrair", methods=["GET", "POST"])
def extrair():
    form = ExtrairForm()
    if request.method == 'POST':
            a = form.link.data
            linkVet.clear()
            tituloVet.clear()
            dataVet.clear()
            scrap(a)
            cont = 0
            while cont <= 19:
                r = ""
                r = Noticia.query.filter_by(link=linkVet[cont]).first()
                if (r is None):
                    r = Noticia(linkVet[cont], tituloVet[cont], dataVet[cont])
                    db.session.add(r)
                    db.session.commit()
                else:
                    r.titulo = tituloVet[cont]
                    r.data   = dataVet[cont]
                    db.session.add(r)
                    db.session.commit()
                cont = cont + 1
            r = Noticia.query.all()
            print(r)
            return render_template('tecmundo.html', linkVet=linkVet, tituloVet=tituloVet, dataVet=dataVet)

    return render_template('extrair.html',
                       form=form)



@app.route('/tecmundo', methods=['GET','POST'])
def tecmundo():
    return render_template('tecmundo.html', linkVet=linkVet, tituloVet=tituloVet, dataVet=dataVet)






