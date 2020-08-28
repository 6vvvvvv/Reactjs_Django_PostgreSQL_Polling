from .models import Polling
from django.http import JsonResponse
import json


def initial(request):
    option_0 = Polling.create_polling(0, "0", 0, 0)
    option_1 = Polling.create_polling(1, "1", 0, 0)
    option_2 = Polling.create_polling(2, "2", 0, 0)

    option_0.save()
    option_1.save()
    option_2.save()

    pollanswer = Polling.objects.all().values()

    return JsonResponse({"msg": "success", "tofrontend": list(pollanswer)})


def polling(request):
    if(request.method == 'POST'):
        frontenddata = json.loads(request.body)
        print("*************frontenddata", frontenddata)

        old_option_0 = Polling.objects.filter(pk=0).values()
        old_option_0_option = old_option_0[0]['option']
        old_option_0_vote = old_option_0[0]['vote']
        old_option_0_rate = old_option_0[0]['rate']

        old_option_1 = Polling.objects.filter(pk=1).values()
        old_option_1_option = old_option_1[0]['option']
        old_option_1_vote = old_option_1[0]['vote']
        old_option_1_rate = old_option_1[0]['rate']

        old_option_2 = Polling.objects.filter(pk=2).values()
        old_option_2_option = old_option_2[0]['option']
        old_option_2_vote = old_option_2[0]['vote']
        old_option_2_rate = old_option_2[0]['rate']

        old_total_vote = old_option_0_vote+old_option_1_vote+old_option_2_vote

        try:
            if(frontenddata['optiondata'][0] == 0):
                # exist alter the title

                # -----------------------------------------------------------------
                # option change
                if(not frontenddata['optiondata'][1] == old_option_0_option):
                    Polling.objects.filter(pk=0).update(
                        option=frontenddata['optiondata'][1], vote=0, rate=0)

                    Polling.objects.filter(pk=1).update(vote=0, rate=0)

                    Polling.objects.filter(pk=2).update(vote=0, rate=0)

                    pollanswer = Polling.objects.all().values()

                    return JsonResponse({"msg": "success", "tofrontend": list(pollanswer)})
                # option stay the same
                else:
                    new_option_0_vote = old_option_0_vote+1
                    new_total_vote = new_option_0_vote+old_option_1_vote+old_option_2_vote
                    new_option_0_rate = new_option_0_vote / new_total_vote

                    new_option_1_rate = old_option_1_vote/new_total_vote

                    new_option_2_rate = old_option_2_vote/new_total_vote

                    Polling.objects.filter(pk=0).update(
                        vote=new_option_0_vote, rate=new_option_0_rate)

                    Polling.objects.filter(pk=1).update(
                        rate=new_option_1_rate)

                    Polling.objects.filter(pk=2).update(
                        rate=new_option_2_rate)

                    pollanswer = Polling.objects.all().values()

                    return JsonResponse({"msg": "success", "tofrontend": list(pollanswer)})

            if(frontenddata['optiondata'][0] == 1):

                # -----------------------------------------------------------------
                # option change
                if(not frontenddata['optiondata'][1] == old_option_1_option):
                    Polling.objects.filter(pk=1).update(
                        option=frontenddata['optiondata'][1], vote=0, rate=0)

                    Polling.objects.filter(pk=0).update(vote=0, rate=0)

                    Polling.objects.filter(pk=2).update(vote=0, rate=0)

                    pollanswer = Polling.objects.all().values()

                    return JsonResponse({"msg": "success", "tofrontend": list(pollanswer)})
                # option stay the same
                else:

                    new_option_1_vote = old_option_1_vote+1
                    new_total_vote = new_option_1_vote+old_option_0_vote+old_option_2_vote

                    new_option_1_rate = new_option_1_vote / new_total_vote

                    new_option_0_rate = old_option_0_vote/new_total_vote

                    new_option_2_rate = old_option_2_vote/new_total_vote

                    Polling.objects.filter(pk=1).update(
                        vote=new_option_1_vote, rate=new_option_1_rate)

                    Polling.objects.filter(pk=0).update(
                        rate=new_option_0_rate)

                    Polling.objects.filter(pk=2).update(
                        rate=new_option_2_rate)

                    pollanswer = Polling.objects.all().values()

                    return JsonResponse({"msg": "success", "tofrontend": list(pollanswer)})

            if(frontenddata['optiondata'][0] == 2):
                # exist alter the title

                # -----------------------------------------------------------------
                # option change
                if(not frontenddata['optiondata'][1] == old_option_2_option):
                    Polling.objects.filter(pk=2).update(
                        option=frontenddata['optiondata'][1], vote=0, rate=0)

                    Polling.objects.filter(pk=1).update(vote=0, rate=0)

                    Polling.objects.filter(pk=0).update(vote=0, rate=0)

                    pollanswer = Polling.objects.all().values()

                    return JsonResponse({"msg": "success", "tofrontend": list(pollanswer)})
                # option stay the same
                else:

                    new_option_2_vote = old_option_2_vote+1

                    new_total_vote = new_option_2_vote+old_option_1_vote+old_option_2_vote

                    new_option_2_rate = new_option_2_vote / new_total_vote

                    new_option_1_rate = old_option_1_vote/new_total_vote

                    new_option_0_rate = old_option_0_vote/new_total_vote

                    Polling.objects.filter(pk=2).update(
                        vote=new_option_2_vote, rate=new_option_2_rate)

                    Polling.objects.filter(pk=1).update(
                        rate=new_option_1_rate)

                    Polling.objects.filter(pk=0).update(
                        rate=new_option_0_rate)

                    pollanswer = Polling.objects.all().values()

                    return JsonResponse({"msg": "success", "tofrontend": list(pollanswer)})

        except Polling.DoesNotExist as identifier:
            print("error---------------------------")
            return JsonResponse({"msg": "fail"})
