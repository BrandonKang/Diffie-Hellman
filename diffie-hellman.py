#-*- coding:utf-8 -*-
#변수 선언
sharedPrime = 23    # p
sharedBase = 5      # g
 
aliceSecret = 4     # a
bobSecret = 3      # b
 
print( "서로가 공유한 소수:" , sharedPrime )
print( "서로가 공유한 기본수" , sharedBase )

print( "\n")

#A = g^a mod p
A = (sharedBase**aliceSecret) % sharedPrime
print( "Alice가 Bob에게 보낸 수: " , A )
 
#B = g^b mod p
B = (sharedBase ** bobSecret) % sharedPrime
print( "Bob이 Alice에게 보낸 수: ", B )

print( "\n")

#Alice의 비밀키 = B^a mod p
aliceSharedSecret = (B ** aliceSecret) % sharedPrime
print( "Alice의 비밀 공유키:", aliceSharedSecret )
 
#Bob의 비밀키 = A^b mod p
bobSharedSecret = (A**bobSecret) % sharedPrime
print( "Bob의 비밀 공유키:", bobSharedSecret )