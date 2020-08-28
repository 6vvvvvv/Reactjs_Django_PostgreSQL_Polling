from .models import Polling
from django.http import JsonResponse
import json


def polling(request):
    if(request.method == 'POST'):
        frontenddata = json.loads(request.body)
        print("*************frontenddata", frontenddata)

        try:
            if(frontenddata['optiondata'][0] == 0):
                # exist alter the title
                if(Polling.objects.filter(pk=0)):

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


                    if((not Polling.objects.filter(pk=1)) and (not Polling.objects.filter(pk=2))):
                        new_option_0_vote = old_option_0_vote+1
                        Polling.objects.filter(pk=0).update(vote=new_option_0_vote)


                    # -----------------------------------------------------------------
                    # option change
                    if(not frontenddata['optiondata'][1] == old_option_0_option):
                        Polling.objects.filter(pk=0).update(
                            option=frontenddata['optiondata'][1], vote=0, rate=0)

                        Polling.objects.filter(pk=1).update(vote=0, rate=0)

                        Polling.objects.filter(pk=2).update(vote=0, rate=0)
                    # option stay the same
                    else:

                        new_option_0_vote = old_option_0_vote+1
                        new_option_0_rate = new_option_0_vote / \
                            (old_total_vote+1)
                        new_total_vote = new_option_0_vote+old_option_1_vote+old_option_2_vote

                        new_option_1_rate = old_option_1_vote/new_total_vote

                        new_option_2_rate = old_option_2_vote/new_total_vote

                        Polling.objects.filter(pk=0).update(
                            vote=new_option_0_vote, rate=new_option_0_rate)

                        Polling.objects.filter(pk=1).update(
                            rate=new_option_1_rate)

                        Polling.objects.filter(pk=2).update(
                            rate=new_option_2_rate)

                # do not exist then  initialization
                else:
                    #################################################!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    if((not Polling.objects.filter(pk=1)) and (not Polling.objects.filter(pk=2))):
                        option_0 = Polling.create_polling(
                            frontenddata['optiondata'][0], frontenddata['optiondata'][1], 1, 1)
                        option_0.save()

                    elif((not Polling.objects.filter(pk=1)) and (Polling.objects.filter(pk=2))):
                        option_2 = Polling.objects.filter(pk=2).values()
                        old_option_2_vote = option_2[0]['vote']

                        new_option_0_rate = format(
                            1/(1+old_option_2_vote), '.2f')

                        option_0 = Polling.create_polling(
                            frontenddata['optiondata'][0], frontenddata['optiondata'][1], 1, new_option_0_rate)

                        option_0.save()

                        new_option_2_rate = 1-new_option_0_rate

                        Polling.objects.filter(pk=2).update(
                            rate=new_option_2_rate)

                    elif((Polling.objects.filter(pk=1)) and (not Polling.objects.filter(pk=2))):
                        option_1 = Polling.objects.filter(pk=1).values()
                        old_option_1_vote = option_1[0]['vote']

                        new_option_0_rate = format(
                            1/(1+old_option_1_vote), '.2f')

                        option_0 = Polling.create_polling(
                            frontenddata['optiondata'][0], frontenddata['optiondata'][1], 1, new_option_0_rate)
                        option_0.save()

                        new_option_1_rate = 1-new_option_0_rate

                        Polling.objects.filter(pk=2).update(
                            rate=new_option_1_rate)

                    else:
                        option_1 = Polling.objects.filter(pk=1).values()
                        old_option_1_vote = option_1[0]['vote']

                        option_2 = Polling.objects.filter(pk=2).values()
                        old_option_2_vote = option_2[0]['vote']

                        new_option_0_rate = format(
                            1/(1 + old_option_1_vote+old_option_2_vote), '.2f')

                        option_0 = Polling.create_polling(
                            frontenddata['optiondata'][0], frontenddata['optiondata'][1], 1, new_option_0_rate)

                        option_0.save()

                        new_option_0 = Polling.objects.filter(
                            pk=0).values()

                        new_option_0_vote = new_option_0[0]['vote']

                        new_option_1_rate = old_option_1_vote / \
                            (new_option_0_vote+old_option_1_vote+old_option_2_vote)

                        new_option_2_rate = old_option_2_vote / \
                            (new_option_0_vote+old_option_1_vote+old_option_2_vote)

                        Polling.objects.filter(pk=1).update(
                            rate=new_option_1_rate)

                        Polling.objects.filter(pk=2).update(
                            rate=new_option_2_rate)

            if(frontenddata['optiondata'][0] == 1):
                if(Polling.objects.filter(pk=1)):

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


                    if((not Polling.objects.filter(pk=0)) and (not Polling.objects.filter(pk=2))):
                        new_option_1_vote = old_option_1_vote+1
                        Polling.objects.filter(pk=1).update(vote=new_option_1_vote)

                    # -----------------------------------------------------------------
                    # option change
                    if(not frontenddata['optiondata'][1] == old_option_1_option):
                        Polling.objects.filter(pk=1).update(
                            option=frontenddata['optiondata'][1], vote=0, rate=0)

                        Polling.objects.filter(pk=0).update(vote=0, rate=0)

                        Polling.objects.filter(pk=2).update(vote=0, rate=0)
                    # option stay the same
                    else:

                        new_option_1_vote = old_option_1_vote+1
                        new_option_1_rate = new_option_1_vote / \
                            (old_total_vote+1)
                        new_total_vote = new_option_1_vote+old_option_0_vote+old_option_2_vote

                        new_option_0_rate = old_option_0_vote/new_total_vote

                        new_option_2_rate = old_option_2_vote/new_total_vote

                        Polling.objects.filter(pk=1).update(
                            vote=new_option_1_vote, rate=new_option_1_rate)

                        Polling.objects.filter(pk=0).update(
                            rate=new_option_0_rate)

                        Polling.objects.filter(pk=2).update(
                            rate=new_option_2_rate)

                # do not exist then  initialization
                else:

                    if((not Polling.objects.filter(pk=0)) and (not Polling.objects.filter(pk=2))):
                        option_1 = Polling.create_polling(
                            frontenddata['optiondata'][0], frontenddata['optiondata'][1], 1, 1)
                        option_1.save()

                    elif((not Polling.objects.filter(pk=0)) and (Polling.objects.filter(pk=2))):
                        option_2 = Polling.objects.filter(pk=2).values()
                        old_option_2_vote = option_2[0]['vote']

                        new_option_1_rate = format(
                            1/(1+old_option_2_vote), '.2f')

                        option_1 = Polling.create_polling(
                            frontenddata['optiondata'][0], frontenddata['optiondata'][1], 1, new_option_1_rate)

                        option_1.save()

                        new_option_2_rate = 1-new_option_1_rate

                        Polling.objects.filter(pk=2).update(
                            rate=new_option_2_rate)

                    elif((Polling.objects.filter(pk=0)) and (not Polling.objects.filter(pk=2))):
                        option_0 = Polling.objects.filter(pk=0).values()
                        old_option_0_vote = option_0[0]['vote']

                        new_option_1_rate = format(
                            1/(1+old_option_0_vote), '.2f')

                        option_1 = Polling.create_polling(
                            frontenddata['optiondata'][0], frontenddata['optiondata'][1], 1, new_option_1_rate)
                        option_1.save()

                        new_option_0_rate = 1-new_option_1_rate

                        Polling.objects.filter(pk=0).update(
                            rate=new_option_0_rate)

                    else:
                        option_0 = Polling.objects.filter(pk=0).values()
                        old_option_0_vote = option_0[0]['vote']

                        option_2 = Polling.objects.filter(pk=2).values()
                        old_option_2_vote = option_2[0]['vote']

                        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

                        new_option_1_rate = format(
                            1/(1 + old_option_0_vote+old_option_2_vote), '.2f')

                        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

                        option_1 = Polling.create_polling(
                            frontenddata['optiondata'][0], frontenddata['optiondata'][1], 1, new_option_1_rate)

                        option_1.save()

                        new_option_1 = Polling.objects.filter(
                            pk=1).values()

                        new_option_1_vote = new_option_1[0]['vote']

                        new_option_0_rate = old_option_0_vote / \
                            (new_option_1_vote+old_option_0_vote+old_option_2_vote)

                        new_option_2_rate = old_option_2_vote / \
                            (new_option_1_vote+old_option_0_vote+old_option_2_vote)

                        Polling.objects.filter(pk=0).update(
                            rate=new_option_0_rate)

                        Polling.objects.filter(pk=2).update(
                            rate=new_option_2_rate)

            if(frontenddata['optiondata'][0] == 2):
                # exist alter the title
                if(Polling.objects.filter(pk=2)):

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

                    if((not Polling.objects.filter(pk=0)) and (not Polling.objects.filter(pk=1))):
                    new_option_2_vote = old_option_2_vote+1
                    Polling.objects.filter(pk=2).update(vote=new_option_2_vote)
                    

                    # -----------------------------------------------------------------
                    # option change
                    if(not frontenddata['optiondata'][1] == old_option_2_option):
                        Polling.objects.filter(pk=2).update(
                            option=frontenddata['optiondata'][1], vote=0, rate=0)

                        Polling.objects.filter(pk=1).update(vote=0, rate=0)

                        Polling.objects.filter(pk=0).update(vote=0, rate=0)
                    # option stay the same
                    else:

                        new_option_2_vote = old_option_2_vote+1
                        new_option_2_rate = new_option_2_vote / \
                            (old_total_vote+1)
                        new_total_vote = new_option_2_vote+old_option_1_vote+old_option_2_vote

                        new_option_1_rate = old_option_1_vote/new_total_vote

                        new_option_0_rate = old_option_0_vote/new_total_vote

                        Polling.objects.filter(pk=2).update(
                            vote=new_option_2_vote, rate=new_option_2_rate)

                        Polling.objects.filter(pk=1).update(
                            rate=new_option_1_rate)

                        Polling.objects.filter(pk=0).update(
                            rate=new_option_0_rate)

                # do not exist then  initialization
                else:

                    if((not Polling.objects.filter(pk=1)) and (not Polling.objects.filter(pk=0))):
                        option_2 = Polling.create_polling(
                            frontenddata['optiondata'][0], frontenddata['optiondata'][1], 1, 1)
                        option_2.save()

                    elif((not Polling.objects.filter(pk=1)) and (Polling.objects.filter(pk=0))):
                        option_0 = Polling.objects.filter(pk=0).values()
                        old_option_0_vote = option_0[0]['vote']

                        new_option_2_rate = format(
                            1/(1+old_option_0_vote), '.2f')

                        option_2 = Polling.create_polling(
                            frontenddata['optiondata'][0], frontenddata['optiondata'][1], 1, new_option_2_rate)

                        option_2.save()

                        new_option_0_rate = 1-new_option_2_rate

                        Polling.objects.filter(pk=0).update(
                            rate=new_option_0_rate)

                    elif((Polling.objects.filter(pk=1)) and (not Polling.objects.filter(pk=0))):
                        option_1 = Polling.objects.filter(pk=1).values()
                        old_option_1_vote = option_1[0]['vote']

                        new_option_2_rate = format(
                            1/(1+old_option_1_vote), '.2f')

                        option_2 = Polling.create_polling(
                            frontenddata['optiondata'][0], frontenddata['optiondata'][1], 1, new_option_2_rate)
                        option_2.save()

                        new_option_1_rate = 1-new_option_2_rate

                        Polling.objects.filter(pk=1).update(
                            rate=new_option_1_rate)

                    else:
                        option_1 = Polling.objects.filter(pk=1).values()
                        old_option_1_vote = option_1[0]['vote']

                        option_0 = Polling.objects.filter(pk=0).values()
                        old_option_0_vote = option_0[0]['vote']

                        new_option_2_rate = format(
                            1/(1 + old_option_1_vote+old_option_0_vote), '.2f')

                        option_2 = Polling.create_polling(
                            frontenddata['optiondata'][0], frontenddata['optiondata'][1], 1, new_option_2_rate)

                        option_2.save()

                        new_option_2 = Polling.objects.filter(
                            pk=2).values()

                        new_option_2_vote = new_option_2[0]['vote']

                        new_option_1_rate = old_option_1_vote / \
                            (new_option_2_vote+old_option_1_vote+old_option_0_vote)

                        new_option_0_rate = old_option_0_vote / \
                            (new_option_2_vote+old_option_1_vote+old_option_0_vote)

                        Polling.objects.filter(pk=1).update(
                            rate=new_option_1_rate)

                        Polling.objects.filter(pk=0).update(
                            rate=new_option_0_rate)

        except Polling.DoesNotExist as identifier:
            print("error---------------------------")

        #     return JsonResponse({"msg": "success", "tofrontend": frontenddata})
