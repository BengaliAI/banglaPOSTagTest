# banglaPOSTagTest
testing bangla postags
```python
Version: 0.0.1     
```
**LOCAL ENVIRONMENT**  
```python
OS          : Ubuntu 18.04.3 LTS (64-bit) Bionic Beaver        
Memory      : 7.7 GiB  
Processor   : Intel® Core™ i5-8250U CPU @ 1.60GHz × 8    
Graphics    : Intel® UHD Graphics 620 (Kabylake GT2)  
Gnome       : 3.28.2  
```
# Setup
**python requirements**
* ```pip3 install -r requirements.txt``` 
> Its better to use a virtual environment 

# Sources
* [**Microsoft India Format Annotation of NLTR DATA**](https://raw.githubusercontent.com/abhishekgupta92/bangla_pos_tagger/master/data/nltr)
* [**ILMT/SketchEngnine Format Annotation of NLTR DATA**](https://firebasestorage.googleapis.com/v0/b/diu-question.appspot.com/o/nlp_data%2Fbn_tagged_mod.txt?alt=media&token=00f383a3-f913-480b-85c1-971dd8fd6dd9)
* [**Pretrained Model** for the second format](https://firebasestorage.googleapis.com/v0/b/diu-question.appspot.com/o/nlp_data%2Fkeras_mlp_bangla.h5?alt=media&token=4146c1b0-1e4d-4f9e-8b2f-7e3519106a40)
* **Resources**: This folder Holds all the resources shared by Mamun sir in the mail thread

# Bangla Test-1: *ILMT_TAGSET_TEST*
* Place the [**Pretrained Model**](https://firebasestorage.googleapis.com/v0/b/diu-question.appspot.com/o/nlp_data%2Fkeras_mlp_bangla.h5?alt=media&token=4146c1b0-1e4d-4f9e-8b2f-7e3519106a40) (**keras_mlp_bangla.h5**) under **tests/ILMT_TAGSET_TEST/**
* testing kernel: **ilmt_test.ipynb**

### **Data EDA**:
* number of senetnces in the dataset:2927
* number of total words in the dataset:40554
* number of unique words in the dataset:12514
* **The word-wise tags and wordcount csv is available at**: ``` /tests/ILMT_TAGSET_TEST/tagged_data_wtc.csv ```
* Tags Found:33 
```python
    'JJ', 'NC', 'PU', 'CCD', 'NP', 
    'VM', 'JQ', 'PRL', 'CX', 'DAB',
    'PPR', 'CSB', 'PP', 'NV', 'CCL', 
    'AMN', 'RDS', 'VAUX', 'NST',
    'ALC', 'PWH', 'RDF', 'PRF', 
    'PRC', 'LC', 'DRL', 'LV', 'DWH', 'CIN',
    'RDX', 'VA', '?', 'CSD'
```
### **Feature Format** (USED FOR THE PRETRAINED MODEL)
* A **tagged_sentence**: defined as the list of tuples of (word,tag) 

> example:[('রপ্তানি', 'JJ'), ('দ্রব্য', 'NC'), ('-', 'PU'), ('তাজা', 'JJ'), ('ও', 'CCD'), ('শুকনা', 'JJ'), ('ফল', 'NC'), (',', 'PU'), ('আফিম', 'NC'), (',', 'PU'), ('পশুচর্ম', 'NC'), ('ও', 'CCD'), ('পশম', 'NC'), ('এবং', 'CCD'), ('কার্পেট', 'NC'), ('৷', 'PU')]

* For the **tagged_sentences** , feature format for each term is as follows : 

```python
    {
        'nb_terms'  : number of terms in the sentence,
        'term'      : the specific term,
        'is_first'  : True if the term is the first one in sentence,
        'is_last'   : True if the term is the last ine in sentence,
        'prefix-1'  : term[0],
        'prefix-2'  : term[:2],
        'prefix-3'  : term[:3],
        'suffix-1'  : term[-1],
        'suffix-2'  : term[-2:],
        'suffix-3'  : term[-3:],
        'prev_word' : the previous word,
        'next_word' : the next word
    }
```
> example: for the term: 'রপ্তানি' the feature construction looks as follows
```python
{
    'nb_terms': 16,
    'term': 'রপ্তানি',
    'is_first': True,
    'is_last': False,
    'prefix-1': 'র',
    'prefix-2': 'রপ',
    'prefix-3': 'রপ্',
    'suffix-1': 'ি',
    'suffix-2': 'নি',
    'suffix-3': 'ানি',
    'prev_word': '',
    'next_word': 'দ্রব্য'
}
```
### **Model Analysis**(BNLTK USED MODEL)
* The model structre is as follows: **(!!!!-Surely we can do better In Shaa Allah)**
```python

Model: "sequential_1" 
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense_1 (Dense)              (None, 512)               24136192  
_________________________________________________________________
activation_1 (Activation)    (None, 512)               0         
_________________________________________________________________
dropout_1 (Dropout)          (None, 512)               0         
_________________________________________________________________
dense_2 (Dense)              (None, 512)               262656    
_________________________________________________________________
activation_2 (Activation)    (None, 512)               0         
_________________________________________________________________
dropout_2 (Dropout)          (None, 512)               0         
_________________________________________________________________
dense_3 (Dense)              (None, 36)                18468     
=================================================================
Total params: 24,417,316
Trainable params: 24,417,316
Non-trainable params: 0
_________________________
```














## Testing Tags

<table style="height: 1065px;" width="538">
<tbody>
<tr>
<td style="width: 190px;">Category</td>
<td style="width: 164px;">Subcategory</td>
<td style="width: 162px;">Part-of-speech tag</td>
</tr>
<tr>
<td style="width: 190px;">NOUN</td>
<td style="width: 164px;">Common</td>
<td style="width: 162px;">NC.*</td>
</tr>
<tr>
<td style="width: 190px;"></td>
<td style="width: 164px;">Proper</td>
<td style="width: 162px;">NP.*</td>
</tr>
<tr>
<td style="width: 190px;"></td>
<td style="width: 164px;">Verbal</td>
<td style="width: 162px;">NV.*</td>
</tr>
<tr>
<td style="width: 190px;"></td>
<td style="width: 164px;">Spatio-temporal</td>
<td style="width: 162px;">NST</td>
</tr>
<tr>
<td style="width: 190px;">VERB</td>
<td style="width: 164px;">Main</td>
<td style="width: 162px;">VM.*</td>
</tr>
<tr>
<td style="width: 190px;"></td>
<td style="width: 164px;">Auxiliary</td>
<td style="width: 162px;">VA.*</td>
</tr>
<tr>
<td style="width: 190px;">PRONOUN</td>
<td style="width: 164px;">Pronominal</td>
<td style="width: 162px;">PPR.*</td>
</tr>
<tr>
<td style="width: 190px;"></td>
<td style="width: 164px;">Reflexive</td>
<td style="width: 162px;">PRF.*</td>
</tr>
<tr>
<td style="width: 190px;"></td>
<td style="width: 164px;">Reciprocal</td>
<td style="width: 162px;">PRC.*</td>
</tr>
<tr>
<td style="width: 190px;"></td>
<td style="width: 164px;">Relative</td>
<td style="width: 162px;">PRL.*</td>
</tr>
<tr>
<td style="width: 190px;"></td>
<td style="width: 164px;">Wh-pronoun</td>
<td style="width: 162px;">PWH.*</td>
</tr>
<tr>
<td style="width: 190px;">NOMINAL MODIFIER</td>
<td style="width: 164px;">Adjective</td>
<td style="width: 162px;">JJ.*</td>
</tr>
<tr>
<td style="width: 190px;"></td>
<td style="width: 164px;">Quantifier</td>
<td style="width: 162px;">JQ.*</td>
</tr>
<tr>
<td style="width: 190px;">DEMONSTRATIVE</td>
<td style="width: 164px;">Absolute</td>
<td style="width: 162px;">DAB.*</td>
</tr>
<tr>
<td style="width: 190px;"></td>
<td style="width: 164px;">Relative</td>
<td style="width: 162px;">DRL.*</td>
</tr>
<tr>
<td style="width: 190px;"></td>
<td style="width: 164px;">Wh</td>
<td style="width: 162px;">DWH.*</td>
</tr>
<tr>
<td style="width: 190px;">ADVERB</td>
<td style="width: 164px;">Manner</td>
<td style="width: 162px;">AMN.*</td>
</tr>
<tr>
<td style="width: 190px;"></td>
<td style="width: 164px;">Location</td>
<td style="width: 162px;">ALC.*</td>
</tr>
<tr>
<td style="width: 190px;">PARTICIPLE</td>
<td style="width: 164px;">Verbal (Adverbial)</td>
<td style="width: 162px;">LV.*</td>
</tr>
<tr>
<td style="width: 190px;"></td>
<td style="width: 164px;">Conditional</td>
<td style="width: 162px;"><span><span class="bluet_tooltip tooltipy-kw tooltipy-kw-4689 tooltipy-kw-cat-786" data-tooltip="4689" style="text-decoration: none; color: rgb(0, 0, 0); border-bottom: 1px dotted rgb(0, 0, 0);">LC</span>.</span>*</td>
</tr>
<tr>
<td style="width: 190px;">PARTICLE</td>
<td style="width: 164px;">Coordinating</td>
<td style="width: 162px;">CCD.*</td>
</tr>
<tr>
<td style="width: 190px;"></td>
<td style="width: 164px;">Subordinating</td>
<td style="width: 162px;">CSB.*</td>
</tr>
<tr>
<td style="width: 190px;"></td>
<td style="width: 164px;">Classifier</td>
<td style="width: 162px;">CCL.*</td>
</tr>
<tr>
<td style="width: 190px;"></td>
<td style="width: 164px;">Interjection</td>
<td style="width: 162px;">CIN.*</td>
</tr>
<tr>
<td style="width: 190px;"></td>
<td style="width: 164px;">Others</td>
<td style="width: 162px;">CX.*</td>
</tr>
<tr>
<td style="width: 360px;" colspan="2">Postposition</td>
<td style="width: 162px;">PP</td>
</tr>
<tr>
<td style="width: 360px;" colspan="2">Punctuation</td>
<td style="width: 162px;">PU</td>
</tr>
<tr>
<td style="width: 190px;">RESIDUAL</td>
<td style="width: 164px;">Foreign word</td>
<td style="width: 162px;">RDF</td>
</tr>
<tr>
<td style="width: 190px;"></td>
<td style="width: 164px;">Symbol</td>
<td style="width: 162px;">RDS</td>
</tr>
<tr>
<td style="width: 190px;"></td>
<td style="width: 164px;">Others</td>
<td style="width: 162px;">RDX</td>
</tr>
</tbody>
</table>




# References
* [Bangla Pos Tagger Based On Conditional Random Fields](https://github.com/abhishekgupta92/bangla_pos_tagger)
* [BNLTK](https://github.com/ashwoolford/bnltk)
* [Sketch Engine Bangla Tagset](https://www.sketchengine.eu/bengali-part-of-speech-tagset/)