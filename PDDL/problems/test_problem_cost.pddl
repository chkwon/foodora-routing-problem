(define (problem test_problem_cost)
  (:domain foodora_cost_domain)
  (:objects c1 c2 c3 - customer
            r1 r2 r3 - restaurant
            b1 b2 b3 - biker
            n1 n2 n3 n4 n5 n6 - node)
  (:init 
  (= (total-cost) 0)
  (at-c c1 n1)
  (at-c c2 n2)
  (at-c c3 n3)
  (at-r r1 n4)
  (at-r r2 n5)
  (at-r r3 n6)
  (edge n1 n2)
  (edge n2 n3)
  (edge n3 n4)
  (edge n4 n5)
  (edge n5 n6)
  (edge n6 n1)
  (= (distance n1 n2) 1)
  (= (distance n2 n3) 5)
  (= (distance n3 n4) 10)
  (= (distance n4 n5) 15)
  (= (distance n5 n6) 20)
  (= (distance n6 n1) 25)
  (at-b b1 n1)
  (at-b b2 n1)
  (at-b b3 n1)
  (rGotFoodFor r1 c1)
  (rGotFoodFor r2 c2)
  (rGotFoodFor r3 c3)
  (notHaveFood b1)
  (notHaveFood b2)
  (notHaveFood b3)
  )
  (:goal (and (gotFood c1) (gotFood c2) (gotFood c3)))
  
  (:metric minimize (total-cost))
  )