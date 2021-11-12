# Signal-Composer-and-Reconstructor
GUI Where you can compose your sinusoidal signal, delete it, sample it, and finally reconstruct it and verifying Nyquist theorem. 

Here is a brief description of our signal composer GUI.

![image](https://user-images.githubusercontent.com/61363974/141429005-d76c4005-09a9-449f-96a0-9b5edb2a52c1.png)

the upper plot is for our current signal we want to add and the lower is for our total signals that we will work on

so lets add some more signal !
![image](https://user-images.githubusercontent.com/61363974/141429466-6921056b-afd3-465b-b273-892d014b2134.png)

But what if we wanted to delete some signals ?
we simply select it from our list and click delete as shown below
![image](https://user-images.githubusercontent.com/61363974/141429741-e8175608-5446-4a5d-b617-81443016dbd6.png)

So now we can either save our signal to load and work on later or add it immediatly to our signal veiwer and reconstractor.
![image](https://user-images.githubusercontent.com/61363974/141430117-30973b46-104f-4a8e-bee3-d93cb2f5c6fd.png)


So here we have our original plot in the upper viewr showing the sampling points a slider to change the sampling frequancy and the lower veiwer is to show our recontracted plot.
![image](https://user-images.githubusercontent.com/61363974/141430518-abf07a80-2919-4532-904f-8b08ae1afdeb.png)

as we can see it didn't reconstrat perfectly as we are selection sampling freq lower than 2fmax

so lets see what if we make it 2fmax
![image](https://user-images.githubusercontent.com/61363974/141430777-42c5b748-a0dc-4ddb-b971-453d21c553da.png)
Reconstracted Perfecly !!

but what if we make our sample freq higher!! 
let's try 3fmax for example
![image](https://user-images.githubusercontent.com/61363974/141430905-0919bf3b-0a64-4a14-8e69-51def7e360d8.png)
Same 2fmax but with more sample points in the upper graph!!

which confirms Nyquist Theorm that all we need to do is sampling with 2fmax to reconstrat our data without losing any information.

finally a bottom to Show/Hide our reconstrated data
![image](https://user-images.githubusercontent.com/61363974/141431441-aea264d4-2454-4a64-a4d4-3abde2f4ab64.png)



