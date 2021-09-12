def convertTocircular(head):
    # declare a node variable
    # start and assign head
    # node into start node.
    start = head
    
    # check that
    while head.next:
    # not equal to null then head
    # points to next node.
        while(head.next is not None):
            head = head.next
            
            #
            if head.next == None:
            # then start assign to the
            # head.next node.
                head.next = start
    return start

    