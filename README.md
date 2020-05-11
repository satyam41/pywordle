<h1> pywordle 💯 </h1>
<h6>wordcloud generator (like the famous tool 'wordle') with python 🐍</h6>

<ul>
  <li>generates words on an image with their size proportional to the frequency of their appearance in the given text file.</li>
  <li><i>currently in development.</i></li>
</ul>

<h4>How to use?</h4>

<ol>
  <li>In it's current state, it can generate words on a canvas based on your selected resolution.</li>
  <li>Just import the project and install PIL fork, then import Image from PIL and assembler in a python script.</li>
  <li>call assembler's assemble function which takes ('filepath_to_read_from', width, height, 'path_to_font', minimum_frequency)</li>
  <li>assemble returns an image, display the image with PIL Image.Image.show() or save it with Image.Image.save()</li>
</ol>

<p><i>As I have now realized that word sizes are unpredictable, try changing the size parameter when calling assemble to see, what fits best.</i></p>
