# Fibonacci_designs
Laser your laptop with a design based on the Fibonacci spiral

This python code produces a design of apple logos for lasering on your macbook.
The pattern includes an apple where the backlit apple logo is, so that the backlit apple
fits into the pattern. REMEMBER TO DELETE THE CENTRAL APPLE BEFORE LASERING YOUR LAPTOP!

Unfortunately, this code produces very large .eps files. Opening them in a vector graphics 
program (e.g. Adobe Illustrator) takes a while, but then saving to .pdf makes the files
much more manageable. For testing purposes, have the code generate a smaller number of apples.

Process:
 1. Play with the settings to get whatever effect you want. Don't use a design that has any apples
  overlapping with the central apple logo, since you will likely end up lasering through the 
  backlit apple logo that's already on your laptop.
 2. Open the .eps file in a vector graphics program and set the artboard size to the 
  dimensions of your laser etcher. Save a copy as a pdf.
 3. Save a second copy of the file, having deleted the central apple and the border rectangle.
 4. Position your laptop in the laser etcher using the first pdf (so you can use the non-cutting
  "line things up" laser on the cutter to position the laptop correctly, matching with the 
  border rectangle and the central apple)
 5. If the central apple isn't lining up well with the border rectangle, play with the 
  center_apple_offset variable below to shift them relative to each other. 
 6. Once everything is lined up, switch to the second pdf (which won't laser through the backlit
  apple and destroy your laptop).
 7. For that matter, maybe it would be a good idea to put a small sheet of something durable over
  the backlit apple logo before you laser anything.
 8. Get the "material thickness" settings correct so that the laser focuses on the top surface of
  your laptop. For mackbook airs, you will need to prop up the front so that the surface doesn't
  slope.
 9. Laser away!

# Use this code and the designs produced by it at your own risk. 
I take no responsibility if you accidentally (or deliberately) destroy your laptop with lasers.
