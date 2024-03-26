#https://github.com/martin-majlis/Wikipedia-API
import wikipediaapi
def sub():
    question='pink floyd'
#   wiki_wiki = wikipediaapi.Wikipedia(question , 'en')
    wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'en')
    page_py = wiki_wiki.page(question)




    print("Page - Title: %s" % page_py.title)
    # Page - Title: Python (programming language)

    print("Page - Summary: %s" % page_py.summary[0:60])
    # Page - Summary: Python is a widely used high-level programming language for

sub()
