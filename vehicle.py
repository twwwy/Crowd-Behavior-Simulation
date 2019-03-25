from setting import *

class Vehicle(object):
    
    def __init__(self, x, y):
        self.position = PVector(x,y)
        self.velocity = PVector(random(-1,1), random(-1,1))
        self.acceleration = PVector(0,0)
        self.r = 4
        self.maxforce = 0.05
        self.maxspeed = random(0.8, 2) 
        
        self.avoidance_weight = 5
        self.cohesion_weight = 0.8
                
    def update(self):
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.maxspeed)
        self.position.add(self.velocity)
        self.acceleration.mult(0)
        
    def seek(self, target):
        desired = PVector.sub(target, self.position)
        desired.setMag(self.maxspeed)
        steer = PVector.sub(desired, self.velocity)
        steer.limit(self.maxforce)
        return steer
    
    def arrive(self, target):
        desired = PVector.sub(target, self.position)
        d = desired.mag()
        if d < 100:
            m = float(map(d, 0, 100, 0, self.maxspeed))
            desired.setMag(m)
        else:
            desired.setMag(self.maxspeed)
        steer = PVector.sub(desired, self.velocity)
        steer.limit(self.maxforce)
        return steer
    
    def separate(self, vehicles):
        desiredseparation = self.r * 3
        sum = PVector()
        count = 0
        for other in vehicles:
            d = PVector.dist(self.position, other.position)
            if d > 0 and d < desiredseparation:
                diff = PVector.sub(self.position, other.position)
                diff.normalize()
                diff.div(d)
                sum.add(diff)
                count += 1
        if count > 0:
            sum.div(count)
            sum.normalize()
            sum.mult(self.maxspeed)
            sum.sub(self.velocity)
            sum.limit(self.maxforce)
        return sum
    
    def alignment(self, vehicles):
        neighbordist = 50
        sum = PVector(0, 0)
        count = 0
        for other in vehicles:
            d = PVector.dist(self.position, other.position)
            if d > 0 and d < neighbordist:
                sum.add(other.velocity)
                count += 1
        if count > 0:
            sum.div(count)
            sum.normalize()
            sum.mult(self.maxspeed)
            steer = PVector.sub(sum, self.velocity)
            steer.limit(self.maxforce)
            return steer
        else:
            return PVector(0, 0)
        
    def cohesion(self, vehicles):
        neighbordist = 50
        sum = PVector(0, 0)
        count = 0
        if len(vehicles) == 1:
            self.cohesion_weight = 2
        for other in vehicles:
            d = PVector.dist(self.position, other.position)
            if d > 0 and d < neighbordist:
                sum.add(other.velocity)
                count += 1
        if count > 0:
            sum.div(count)
            return self.seek(sum)
        else:
            return PVector(0, 0)
    
    def avoidance(self, vehicles):
        c = -13312
        R = self.r * 4
        Dis = 10
        left_theta = -0.3
        right_theta = 0.3
        
        predict = self.velocity.get()
        predict.normalize()
        predict.mult(Dis)
        predict.add(self.position) #future position
        
        h = self.velocity.heading2D()
        
        left = PVector(R * cos(h + left_theta), R * sin(h + left_theta))
        right = PVector(R * cos(h + right_theta), R * sin(h + right_theta))
        
        left_pos = PVector.add(predict, left)
        right_pos = PVector.add(predict, right)
        
        #noFill()
        #noStroke()
        #ellipse(int(left_pos.x), int(left_pos.y), 5, 5)
        #ellipse(int(right_pos.x), int(right_pos.y), 5, 5)
        
        
        if get(int(left_pos.x), int(left_pos.y)) != c and get(int(right_pos.x), int(right_pos.y)) == c:
            self.avoidance_weight = 5
            return self.seek(left_pos)
        elif get(int(left_pos.x), int(left_pos.y)) == c and get(int(right_pos.x), int(right_pos.y)) != c:
            self.avoidance_weight = 5
            return self.seek(right_pos)
        elif get(int(left_pos.x), int(left_pos.y)) == c and get(int(right_pos.x), int(right_pos.y)) == c:
            turns = [left_pos, right_pos]
            self.avoidance_weight = 10
            self.velocity = self.velocity / 10
            return self.seek(turns[int(random(2))])
        else:
            self.avoidance_weight = 1
            return PVector(0, 0)
            
        
    
    def applyForce(self, force):
        self.acceleration.add(force)
    
    def dynamics(self):
        pass
    
    
    def applyBehaviors(self, vehicles, target):
        arriveForce = self.arrive(target)
        separateForce = self.separate(boids)
        cohesionForce = self.cohesion(boids)
        alignmentForce = self.alignment(vehicles)
        avoidanceForce = self.avoidance(vehicles)
        
        arriveForce.mult(1)
        separateForce.mult(2)
        cohesionForce.mult(self.cohesion_weight)
        alignmentForce.mult(1)
        avoidanceForce.mult(self.avoidance_weight)
        
        self.applyForce(arriveForce)
        self.applyForce(separateForce)
        self.applyForce(cohesionForce)
        self.applyForce(alignmentForce)
        self.applyForce(avoidanceForce)
                                  
                                  
    def borders(self):
        if self.position.x < -self.r:
            self.position.x = width + self.r
        if self.position.y < -self.r:
            self.position.y = height + self.r
        if self.position.x > width + self.r:
            self.position.x = -self.r
        if self.position.y > height + self.r:
            self.position.y = -self.r
            
    
    def display(self, color_int):
        theta = float(self.velocity.heading2D() + PI/2)
        fill(color_int);
        stroke(0);
        strokeWeight(1);
        pushMatrix();
        translate(self.position.x, self.position.y);
        rotate(theta);
        beginShape();
        vertex(0, -self.r*2);
        vertex(-self.r, self.r*2);
        vertex(self.r, self.r*2);
        endShape(CLOSE);
        popMatrix();
        
    def run(self, vehicles, target, color_int=127):
        self.applyBehaviors(vehicles, target)
        self.update()
        self.borders()
        self.display(color_int)
        
