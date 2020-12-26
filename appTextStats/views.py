from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
from TextStatistics.settings import FILE_DIR
from appTextStats.parser.wordCount import TextParser
from appTextStats.parser.specialChar import SpecialCharParser
from appTextStats.parser.removeChar import RemoveCharParser

# Create your views here.
@csrf_exempt
def perform_stats(request):
    print(request)
    textDict = {}
    params = json.loads(request.body)
    document = params['file_name']
    print(document)
    id = params['id']
    id = str(id)
    
    uploaded_path = os.path.join(FILE_DIR,'user_'+id +'/rawData/' + document)
    try:
        os.mkdir(FILE_DIR+'/user_'+id +'/textStatsData/')
    except Exception as err:
        print('Mkdir Error : {0}'.format(err))

    textStats_path = os.path.join(FILE_DIR,'user_'+id +'/textStatsData/' + document)
    #print(uploaded_path)
    parserop = TextParser()
    textDict = parserop.parse(uploaded_path)

    wf = open(textStats_path,'w')
    for k,v in textDict.items():
        if k == 'nl':
            print('Total no of lines(including Blank) : '+str(v),file=wf)
        if k == 'l':
            print('Total no of lines : '+str(v),file=wf)
        if k == 'wc':
            print('Total no of words : '+str(v),file=wf)
        if k == 'tu':
            print('************************************************************',file=wf)
            print('Word : Count',file=wf)
            for val in v:
                print(val[0] +' : ' + str(val[1]),file=wf)
    wf.close

    return JsonResponse(data={'status' : 200})


@csrf_exempt
def perform_removeChar(request):
    print(request)
    textDict = {}
    params = json.loads(request.body)
    document = params['file_name']
    remove_char = params['remove_char']
    print(document)
    id = params['id']
    id = str(id)
    
    uploaded_path = os.path.join(FILE_DIR,'user_'+id +'/rawData/' + document)
    try:
        os.mkdir(FILE_DIR+'/user_'+id +'/removeCharData/')
    except Exception as err:
        print('Mkdir Error : {0}'.format(err))

    removeChar_path = os.path.join(FILE_DIR,'user_'+id +'/removeCharData/' + document)
    #print(uploaded_path)
    parserop = RemoveCharParser()
    textDict = parserop.parse(uploaded_path,remove_char)

    wf = open(removeChar_path,'w')
    
    #print(textDict['removeChar'],file=wf)

    wf.close

    return JsonResponse(data={'status' : 200})


@csrf_exempt
def perform_specialChar(request):
    params = json.loads(request.body)
    document = params['file_name']
    id = params['id']
    id = str(id)
    
    uploaded_path = os.path.join(FILE_DIR,'user_'+id +'/rawData/' + document)
    #print(uploaded_path)
    parserop = SpecialCharParser()

    specialChar = parserop.parse(uploaded_path)
    #print(specialChar)
    return JsonResponse(data=specialChar)








    

