true = 'true'
test = {
   "results": [
      {
         "alternatives": [
            {
               "confidence": 0.674,
               "transcript": "안녕하세요 "
            },
            {
               "transcript": "안녕하세여 "
            }
         ],
         "final": true
      }
   ],
   "result_index": 0
}
# print(type(test))
# print(test['results'][0]['alternatives'])
result =[]
num = 0
for i in test['results'][0]['alternatives']:
        result.insert(num,str(i["transcript"]))
        num +=1

print (result)