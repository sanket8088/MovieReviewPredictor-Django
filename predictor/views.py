from django.shortcuts import render
import pickle
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from django.http import JsonResponse
import json


# Create your views here.


def home(request):
    return render(request,"predictor/index.html")

@csrf_exempt  
def predictor(request):
    if request.method == "POST":
        myStatement = json.loads(json.dumps(dict(request.POST)))
        # import pdb; pdb.set_trace()
        statement = myStatement["statement"][0]
        with open('randomForestCv', 'rb') as f:
            cv, rfc, ln = pickle.load(f)
        test = statement.lower()
        test = test.replace("[^a-z]", " ")
        stop_words = stopwords.words("english")
        test = [word for word in test if word not in stop_words]
        word_lemmat=WordNetLemmatizer()
        test = [word_lemmat.lemmatize(word) for word in test]
        ps=PorterStemmer()
        test = " ".join([ps.stem(word) for word in test])
        test = [test]
        to_transform = cv.transform(test).toarray()
        a = rfc.predict(to_transform)
        print(a)
        a=ln.inverse_transform(a)
        print(a)
        js=json.dumps({"value" : a[0]})
        return JsonResponse(js, safe=False)

        