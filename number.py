# Although this number looks transcendental, this would be extremely hard to prove. I will write a second program that converts to hexadecimal.
n=0 # set the n to 0 for initialization
echo -n 0. # allow this to be a number
while n=$(( $n + 1 )); do # just keep going until stopped
        echo $n | python rand.py | tr -d \\n | tee $1 #
done
