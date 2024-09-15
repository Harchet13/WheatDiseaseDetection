from ultralytics import YOLO
import streamlit as st
from PIL import Image
import streamlit_analytics

st.set_page_config(page_title="WheatCheck",page_icon="WheatCheck clear logo.png",layout="wide")

with streamlit_analytics.track():
	st.markdown('''
    	<style>
    	.st-emotion-cache-1jzia57.e1nzilvr2 #danger-zone
    	{
        display: none;
    	}
    	.st-emotion-cache-1r7h7mk.eqpbllx1
    	{
        display: none;
    	}
    	</style>
    	''',unsafe_allow_html=True)
	
	def set_language():
	    if f"selected_language" in st.session_state:
	        lang = st.session_state[f"selected_language"]
	        # st.experimental_set_query_params(**{f"lang": lang})
	        return lang
	    return "English"

	# Load the model
	@st.cache_resource
	def models():
	    mod = YOLO('best.pt')
	    return mod
	
	languages = ["English", "Tiếng Việt"]
	sel_lang = st.radio(
		"Language",
		options=languages,
		horizontal=True,
		key="selected_language",
	)
	selected_language = set_language()
	
	st.markdown(f"Selected Language: {selected_language}")
	
	# Logo and title section
	with st.container():
	    col = st.columns([3,9])
	    col[0].image('logo.png')
	    col[1].text('')
	    col[1].text('')
	    col[1].text('')
	    col[1].text('')
	    if selected_language == "English":
	        col[1].markdown("<h1 style='text-align: center; color: white;'>WheatCheck - Wheat Disease Detection</h1>", unsafe_allow_html=True)
	    elif selected_language == "Tiếng Việt":
	        col[1].markdown("<h1 style='text-align: center; color: white;'>वीटचेक - गेहूँ रोग का पता लगाये</h1>", unsafe_allow_html=True)

	
	if selected_language == "English":
	    # About the app section
	    with st.container():
	        st.header('Safeguarding Global Food Security')
	        st.write('''Wheat is one of the most vital crops for human consumption, feeding billions of people worldwide. 
  		However, this essential crop is under constant threat from a wide range of diseases caused by pathogens and pests. 
    		Every year, these threats result in significant losses—equivalent to 21.5% of global wheat production. 
      		This translates to an astonishing 209 million tonnes of wheat, valued at an estimated $31 billion, lost annually.''')
	        st.subheader('Understanding the Challenge')
	        st.write('''The challenge of wheat disease is multifaceted. Wheat crops are susceptible to various pathogens, including fungi, bacteria, viruses, and pests, 
  		each capable of devastating entire fields if not detected and managed early. 
    		Diseases like rusts, mildew, and blight, alongside pests like aphids and stem flies, can drastically reduce yield quality and quantity. 
      		The economic impact is profound, affecting not only farmers but also the global food supply chain, 
		leading to increased prices and food insecurity in vulnerable regions.''')
		
	elif selected_language == "Tiếng VIệt":
	    # About the app section
	    with st.container():
	        st.header('वैश्विक खाद्य सुरक्षा की रक्षा करना')
	        st.write('''गेहूं मानव उपभोग के लिए सबसे महत्वपूर्ण फसलों में से एक है, जो दुनिया भर में अरबों लोगों का पेट भरता है। 
  		हालाँकि, यह आवश्यक फसल रोगजनकों और कीटों के कारण होने वाली विभिन्न प्रकार की बीमारियों से लगातार खतरे में है। 
    		हर साल, इन खतरों के परिणामस्वरूप महत्वपूर्ण नुकसान होता है - जो वैश्विक गेहूं उत्पादन के 21.5% के बराबर है। 
      		इसका मतलब है कि आश्चर्यजनक रूप से 209 मिलियन टन गेहूं, जिसकी अनुमानित कीमत 31 बिलियन डॉलर है, हर साल नष्ट हो जाता है।''')
	        st.subheader('चुनौती को समझना')
	        st.write('''गेहूं की बीमारी की चुनौती बहुआयामी है। गेहूं की फसलें कवक, बैक्टीरिया, वायरस और कीटों सहित विभिन्न रोगजनकों के प्रति संवेदनशील होती हैं। 
  		यदि शीघ्र पता नहीं लगाया गया और प्रबंधित नहीं किया गया तो प्रत्येक पूरे क्षेत्र को तबाह करने में सक्षम है। 
    		एफिड्स और तना मक्खियों जैसे कीटों के साथ-साथ जंग, फफूंदी और झुलसा जैसी बीमारियाँ उपज की गुणवत्ता और मात्रा को काफी कम कर सकती हैं। 
      		आर्थिक प्रभाव गहरा है, न केवल किसानों को बल्कि वैश्विक खाद्य आपूर्ति श्रृंखला को भी प्रभावित कर रहा है। 
		जिससे कमजोर क्षेत्रों में कीमतें बढ़ीं और खाद्य असुरक्षा पैदा हुई।''')
		    


	# Display disease images with captions
	if selected_language == "English":
		col = st.columns(7)
		with col[0]:
			st.image('aphid_1.jpeg', caption='Aphid')
		with col[1]:
		        st.image('brown_rust_3.jpeg', caption='Brown Rust')
		with col[2]:
			st.image('mite_26.jpeg', caption='Mite')
		with col[3]:
		        st.image('stem_fly_30.jpeg', caption='Stem Fly')
		with col[4]:
		        st.image('black_rust_1.jpeg', caption='Black Rust')
		with col[5]:
		        st.image('common_root_rot_55.jpeg', caption='Common Root Rot')
		with col[6]:
		        st.image('leaf_blight_38.jpeg', caption='Leaf Blight')
			
		col1 = st.columns(7)
		with col1[0]:
		        st.image('septoria_5.jpeg.png', caption='Septoria')
		with col1[1]:
		        st.image('tan_spot_24.jpeg', caption='Tan Spot')
		with col1[2]:
		        st.image('blast_1.jpeg', caption='Blast')
		with col1[3]:
		        st.image('fusarium_head_blight_test_0.png', caption='Fusarium Head Blight')
		with col1[4]:
		        st.image('mildew_82.png', caption='Mildew')
		with col1[5]:
		        st.image('smut_test_0.png', caption='Smut')
		with col1[6]:
		        st.image('yellow_rust_256.png', caption='Yellow Rust')
		
	elif selected_language == "Tiếng VIệt":
		col = st.columns(7)
		with col[0]:
			st.image('aphid_1.jpeg', caption='एफिड')
		with col[1]:
		        st.image('brown_rust_3.jpeg', caption='भूरा जंग')
		with col[2]:
			st.image('mite_26.jpeg', caption='घुन')
		with col[3]:
		        st.image('stem_fly_30.jpeg', caption='तना मक्खी')
		with col[4]:
		        st.image('black_rust_1.jpeg', caption='काला जंग')
		with col[5]:
		        st.image('common_root_rot_55.jpeg', caption='सामान्य जड़ सड़न')
		with col[6]:
		        st.image('leaf_blight_38.jpeg', caption='पत्ती का झुलसा रोग')
			
		col1 = st.columns(7)
		with col1[0]:
		        st.image('septoria_5.jpeg.png', caption='सेप्टोरिया')
		with col1[1]:
		        st.image('tan_spot_24.jpeg', caption='टैन स्पॉट')
		with col1[2]:
		        st.image('blast_1.jpeg', caption='ब्लास्ट')
		with col1[3]:
		        st.image('fusarium_head_blight_test_0.png', caption='फ्यूजेरियम हेड ब्लाइट')
		with col1[4]:
		        st.image('mildew_82.png', caption='फफूंदी')
		with col1[5]:
		        st.image('smut_test_0.png', caption='मैल')
		with col1[6]:
		        st.image('yellow_rust_256.png', caption='पीला रतुआ')

	

	if selected_language == "English":
		st.subheader('The Role of Technology in Early Detection')
		st.write('''In response to these challenges, technology offers a powerful solution. 
	  	The Wheat Detection web app harnesses the power of artificial intelligence and machine learning to identify diseases in wheat crops at an early stage. 
	    	By analyzing images of wheat fields, the app can accurately detect signs of disease, enabling farmers to take prompt action. 
	      	Early detection is critical in preventing the spread of disease, protecting crop yields, and ensuring a stable food supply.''')
		st.image('farmer.webp')
		st.subheader('How It Works')
		st.markdown('''
		1. Image Capture: Farmers capture images of their wheat fields using a smartphone or drone.
		2. Analysis: The app processes these images using advanced machine learning algorithms trained to recognize specific disease patterns.
		3. Diagnosis: The app provides an instant diagnosis, identifying the type of disease and offering suggestions for treatment.
		4. Actionable Insights: Farmers receive recommendations on how to manage the detected disease, including optimal pesticide use and agronomic practices to mitigate the impact.''')
		st.subheader('The Impact')
		st.write('By integrating this technology into their farming practices, farmers can significantly reduce the losses caused by wheat diseases. The Wheat Detection app not only helps in preserving crop yields but also contributes to global efforts in achieving food security and reducing hunger. The economic benefits are also substantial, allowing farmers to maximize their profits and ensuring that the wheat market remains stable.')
		st.subheader('Join the Movement')
		st.write('As we move towards a future where technology plays an integral role in agriculture, the Wheat Detection app is at the forefront of this revolution. Join us in protecting one of the world’s most important crops and securing the future of global food security.')
		
		st.subheader('Steps to use the app')
		st.markdown('''
		- Take a clear image
		- Upload the image
		- Analyze the image and the name and confidence level of the disease along with the causes, preventions, and remedies will be displayed in the result panel below''')
		
		
