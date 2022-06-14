import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Auction, Bider
# Create your views here.
def auction(request):
    auctions = Auction.objects.all()
    context = {
        'auctions':auctions
    }
    return render(request, 'auction/auction.html', context)



def bidding(request, id):
    auction = Auction.objects.get(id=id)
    auctions =  Bider.objects.filter(auction=auction)
    highest_bid = max(auctions.values_list('amount', flat=True), default=0)
    latest_bid =  Bider.objects.filter(user=request.user, auction=auction).last()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        highest_bid_s = round(highest_bid, 1)
        return JsonResponse(highest_bid_s,safe=False)

    context =  {
        'data':auction,
        'latest_bid':latest_bid,
        'highest_bid':highest_bid
    }
    return render(request, 'auction/bidding.html', context)




def add_bid(request):
    if request.method == 'POST':
        print(request.POST)
        amount = request.POST.get('the_amount')
        auction = request.POST.get('the_auction')
        response_data = {}

        bid = Bider(amount=amount, auction_id=auction, user=request.user)
        bid.save()

        response_data['result'] = 'BID SUBMITTED'
        response_data['bid_id'] = bid.pk
        response_data['amount'] = bid.amount
        response_data['auction'] = bid.auction_id
        response_data['bider'] = bid.user.username

        return HttpResponse(
            json.dumps(response_data),
            content_type = "application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"Error":"Failed to submit"}),
            content_type = 'application/json'

        )