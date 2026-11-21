(function(){
'use strict';
var store={get:function(k){try{return localStorage.getItem('lx:'+k)}catch(e){return null}},set:function(k,v){try{localStorage.setItem('lx:'+k,v)}catch(e){}},del:function(k){try{localStorage.removeItem('lx:'+k)}catch(e){}}};
var $=function(s,r){return (r||document).querySelector(s)},$$=function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))};
var esc=function(s){return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})};
var DOCENT=/[?&]docent\b/.test(location.search);
if(DOCENT){$('#docentbar').hidden=false}

/* toast */
var tt;function toast(m){var t=$('#toast');t.textContent=m;t.hidden=false;clearTimeout(tt);tt=setTimeout(function(){t.hidden=true},3600)}

/* theme */
var root=document.documentElement;
var saved=store.get('theme');
root.setAttribute('data-theme',saved||(window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'));
function themeIcon(){$('#theme').textContent=root.getAttribute('data-theme')==='dark'?'☀️':'🌙'}
$('#theme').addEventListener('click',function(){var t=root.getAttribute('data-theme')==='dark'?'light':'dark';root.setAttribute('data-theme',t);store.set('theme',t);themeIcon()});
themeIcon();

/* router */
var pages=$$('.page'),pendingAnchor=null;
var panel=$('#chpanel');
var side=$('#side'),narrow=function(){return window.innerWidth<1000};
function setSide(on,save){fitSide();document.body.classList.toggle('side-on',on);$('#chbtn').setAttribute('aria-expanded',on);if(save)store.set('side',on?'1':'0')}
function fitSide(){var tb=document.querySelector('.topbar');document.documentElement.style.setProperty('--tb',tb.offsetHeight+'px')}
window.addEventListener('resize',fitSide);window.addEventListener('load',fitSide);
setSide(narrow()?false:store.get('side')!=='0',false);
$('#chbtn').addEventListener('click',function(){setSide(!document.body.classList.contains('side-on'),!narrow())});
$('#sideback').addEventListener('click',function(){setSide(false,false)});
$('#sideopen').addEventListener('click',function(){$$('#side details').forEach(function(d){d.open=true})});
$('#sideclose').addEventListener('click',function(){$$('#side details').forEach(function(d){d.open=false})});
side.addEventListener('click',function(e){if(narrow()&&e.target.closest('a'))setSide(false,false)});
function parse(){var h=(location.hash||'#home').replace('#','');var p=h.split('/');if(p[0]==='home'||!p[0])return{chap:null,page:'home',id:'p-home'};return{chap:p[0],page:p[1]||'start',id:'p-'+p[0]+'-'+(p[1]||'start')}}
function show(){
  var r=parse(),el=document.getElementById(r.id);
  if(!el){location.hash='#home';return}
  pages.forEach(function(p){p.classList.toggle('active',p===el)});
  $$('nav.tabs').forEach(function(n){n.classList.toggle('on',n.dataset.chap===r.chap)});
  $$('nav.tabs a').forEach(function(a){a.classList.toggle('active',a.getAttribute('href')==='#'+r.chap+'/'+r.page)});
  $$('#side details').forEach(function(d){var on=d.dataset.chap===r.chap;d.classList.toggle('cur',on);if(on)d.open=true});
  $$('#side details a').forEach(function(a){a.classList.toggle('active',a.getAttribute('href')==='#'+r.chap+'/'+r.page)});
  $$('#chpanel a').forEach(function(a){a.classList.toggle('cur',a.getAttribute('href').indexOf('#'+r.chap+'/')===0)});
  var cur=$('nav.tabs.on a.active');if(cur&&cur.scrollIntoView&&cur.parentNode.scrollWidth>cur.parentNode.clientWidth)cur.scrollIntoView({inline:'center',block:'nearest'});
  if(r.chap)store.set('last',location.hash);
  if(pendingAnchor){var t=document.getElementById(pendingAnchor);pendingAnchor=null;if(t){t.scrollIntoView();t.classList.add('flash');setTimeout(function(){t.classList.remove('flash')},1800);scrollSpy();return}}
  window.scrollTo(0,0);scrollSpy();
  if(r.chap===null)homeUpdate();
}
window.addEventListener('hashchange',show);

/* scroll progress + toc spy */
function scrollSpy(){
  var d=document.documentElement,max=d.scrollHeight-innerHeight;
  $('.progressbar i').style.width=(max>0?Math.min(100,scrollY/max*100):0)+'%';
  var page=$('.page.active');if(!page)return;
  var links=$$('.toc a',page);if(!links.length)return;
  var cur=null;
  links.forEach(function(a){var t=document.getElementById(a.getAttribute('href').slice(1));if(t&&t.getBoundingClientRect().top<140)cur=a});
  links.forEach(function(a){a.classList.toggle('on',a===cur)});
}
window.addEventListener('scroll',scrollSpy,{passive:true});
$$('.toc a').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();var t=document.getElementById(a.getAttribute('href').slice(1));if(t)t.scrollIntoView({behavior:'smooth'})})});

/* copy buttons (gedelegeerd) */
document.addEventListener('click',function(e){
  var b=e.target.closest('.copy');if(!b)return;
  var txt=b.dataset.copy;
  function ok(){b.textContent='✓ Gekopieerd';b.classList.add('ok');setTimeout(function(){b.textContent='Kopieer';b.classList.remove('ok')},1400)}
  function fallback(){var ta=document.createElement('textarea');ta.value=txt;ta.style.position='fixed';ta.style.opacity='0';document.body.appendChild(ta);ta.select();try{document.execCommand('copy');ok()}catch(err){}document.body.removeChild(ta)}
  if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(txt).then(ok,fallback)}else fallback();
});

/* lightbox */
document.addEventListener('click',function(e){
  var im=e.target.closest('figure img');var lb=$('#lightbox');
  if(im){$('img',lb).src=im.src;lb.hidden=false;return}
  if(e.target.closest('#lightbox'))lb.hidden=true;
});

/* afdrukken */
document.addEventListener('click',function(e){if(e.target.closest('.printbtn'))window.print()});

/* doelstellingen-checklist per hoofdstuk */
$$('.p-start').forEach(function(pg){
  var num=pg.dataset.pid.split('-')[0];
  var h=$$('h2',pg).filter(function(x){return /doelstellingen/i.test(x.textContent)})[0];if(!h)return;
  var ol=h.nextElementSibling;while(ol&&ol.tagName!=='OL')ol=ol.nextElementSibling;if(!ol)return;
  ol.classList.add('goals');
  $$('li',ol).forEach(function(li,i){
    var key='goal-'+num+'-'+i,cb=document.createElement('input');cb.type='checkbox';cb.checked=store.get(key)==='1';
    li.insertBefore(cb,li.firstChild);li.classList.toggle('on',cb.checked);
    function upd(){li.classList.toggle('on',cb.checked);store.set(key,cb.checked?'1':'0')}
    cb.addEventListener('change',upd);
    li.addEventListener('click',function(e){if(e.target!==cb&&e.target.tagName!=='CODE'&&e.target.tagName!=='KBD'){cb.checked=!cb.checked;upd()}});
  });
});

/* oefeningen: klaar / overslaan en vergrendelde oplossingen */
var SETS=$$('.exset');
SETS.forEach(function(set){
  var units=$$('.ex',set),n=units.length,hassol=set.dataset.hassol==='1';
  var cnt=$('.cnt',set),meter=$('.meter i',set),msg=$('.lockmsg',set),showall=$('.showall',set);
  if(!hassol)set.classList.add('nosol');
  function setState(u,s){u.classList.toggle('done',s==='done');u.classList.toggle('skip',s==='skip')}
  function refresh(){
    var d=units.filter(function(u){return u.classList.contains('done')||u.classList.contains('skip')}).length;
    var all=d===n;var unlocked=!hassol||all||DOCENT;
    set.classList.toggle('unlocked',unlocked);
    cnt.textContent=d+' / '+n+' afgewerkt';meter.style.width=(n?d/n*100:0)+'%';
    if(hassol){msg.textContent=unlocked?(all?'🔓 Alle oefeningen afgewerkt: de oplossingen zijn ontgrendeld.':'🔓 Docentenmodus: oplossingen ontgrendeld.'):'🔒 Oplossingen zijn vergrendeld tot je alle oefeningen als klaar of overgeslagen hebt gemarkeerd (nog '+(n-d)+').'}
    showall.hidden=!(hassol&&unlocked);
    if(!unlocked)$$('details',set).forEach(function(x){x.open=false});
    homeUpdate();
  }
  units.forEach(function(u){
    var key='ex-'+u.dataset.ex;setState(u,store.get(key)||'');
    $$('.st',u).forEach(function(b){b.addEventListener('click',function(){
      var want=b.dataset.act,cur=u.classList.contains('done')?'done':(u.classList.contains('skip')?'skip':'');
      var ns=cur===want?'':want;setState(u,ns);if(ns)store.set(key,ns);else store.del(key);refresh();
    })});
  });
  set.addEventListener('click',function(e){
    var s=e.target.closest('summary');
    if(s&&!set.classList.contains('unlocked')){e.preventDefault();toast('Rond eerst alle oefeningen van deze set af (klaar of overgeslagen). Een oefening overslaan mag.')}
  });
  $('.reset',set).addEventListener('click',function(){if(!confirm('Voortgang van deze set wissen?'))return;units.forEach(function(u){setState(u,'');store.del('ex-'+u.dataset.ex)});refresh()});
  showall.addEventListener('click',function(){var ds=$$('details',set);var any=ds.some(function(x){return !x.open});ds.forEach(function(x){x.open=any});showall.textContent=any?'Alle oplossingen verbergen':'Alle oplossingen tonen'});
  refresh();
});

/* startpagina: voortgang */
function homeUpdate(){
  var tot=0,dn=0;
  $$('.chcard').forEach(function(c){
    var num=c.dataset.chap,us=$$('#p-'+num+'-oefeningen .ex');
    var d=us.filter(function(u){return u.classList.contains('done')||u.classList.contains('skip')}).length;
    var bx=$('.cprog',c);
    if(us.length){bx.hidden=false;$('i',bx).style.width=(d/us.length*100)+'%';$('span',bx).textContent=d+'/'+us.length;tot+=us.length;dn+=d}
    var chip=$('#chips-'+num);if(chip&&us.length){chip.textContent='✅ '+d+'/'+us.length+' afgewerkt'}
  });
  $('#overall-meter').style.width=(tot?dn/tot*100:0)+'%';
  $('#overall-label').textContent='Totale voortgang oefeningen: '+dn+' / '+tot;
  var last=store.get('last'),r=$('#resume');
  if(last){r.hidden=false;r.href=last;var m=last.replace('#','').split('/');var t=$('#chpanel a[href^="#'+m[0]+'/"]');r.textContent='Verder waar je gebleven was ('+(t?t.textContent:m[0])+') →'}
}
$('#resetall').addEventListener('click',function(){
  if(!confirm('Alle voortgang wissen (oefeningen, doelstellingen)?'))return;
  try{Object.keys(localStorage).filter(function(k){return k.indexOf('lx:ex-')===0||k.indexOf('lx:goal-')===0||k==='lx:last'}).forEach(function(k){localStorage.removeItem(k)})}catch(e){}
  location.reload();
});

/* kennistoetsen: per pagina */
function shuffle(a){for(var i=a.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1));var t=a[i];a[i]=a[j];a[j]=t}return a}
$$('.page').forEach(function(pg){
  var qs=$$('.q',pg);if(!qs.length)return;
  var lab=$('.sc-label',pg),mt=$('.sc-meter',pg);
  function score(){var g=qs.filter(function(q){return q.classList.contains('ok')}).length;var a=qs.filter(function(q){return q.classList.contains('ok')||q.classList.contains('bad')}).length;
    lab.textContent=g+' / '+qs.length+' juist'+(a<qs.length?' · '+(qs.length-a)+' te gaan':' · klaar!');mt.style.width=(g/qs.length*100)+'%'}
  qs.forEach(function(q,idx){
    var n=$('.qt .n',q);if(n)n.textContent=idx+1;
    var type=q.dataset.type;
    if(type==='quiz'){
      var correct=+q.dataset.correct,exp=$('.explain',q);
      $$('.opt',q).forEach(function(b,i){b.addEventListener('click',function(){
        if(q.classList.contains('ok')||q.classList.contains('bad'))return;
        var okk=i===correct;q.classList.add(okk?'ok':'bad');
        $$('.opt',q).forEach(function(x,j){x.disabled=true;if(j===correct)x.classList.add('right')});
        if(!okk)b.classList.add('wrong');
        exp.hidden=false;score();
      })});
      $('.retry',q).addEventListener('click',function(){q.classList.remove('ok','bad');$$('.opt',q).forEach(function(x){x.disabled=false;x.classList.remove('right','wrong')});exp.hidden=true;score()});
    }else if(type==='match'){
      var ans=JSON.parse(q.dataset.answers),all=JSON.parse(q.dataset.all);
      $$('.matchrow',q).forEach(function(r){var sel=$('select',r);shuffle(all.slice()).forEach(function(t){var o=document.createElement('option');o.textContent=t;o.value=t;sel.appendChild(o)});sel.selectedIndex=0});
      $('.check',q).addEventListener('click',function(){
        var okAll=true,empty=false;
        $$('.matchrow',q).forEach(function(r,i){var v=$('select',r).value;var okk=v===ans[i];if(!v)empty=true;if(!okk)okAll=false;
          r.classList.remove('good','fail');if(v){r.classList.add(okk?'good':'fail')}$('.mark',r).textContent=v?(okk?'✅':'❌'):''});
        q.classList.remove('ok','bad');if(okAll)q.classList.add('ok');else if(!empty)q.classList.add('bad');
        $('.fb',q).textContent=okAll?'Alles juist!':(empty?'Kies bij elke term een antwoord.':'Nog niet helemaal. Verbeter de rode regels en controleer opnieuw.');
        $('.fb',q).className='fb '+(okAll?'ok':'bad');score();
      });
      $('.show',q).addEventListener('click',function(){$$('.matchrow',q).forEach(function(r,i){$('select',r).value=ans[i];r.classList.remove('fail');r.classList.add('good');$('.mark',r).textContent='✅'});q.classList.remove('bad');$('.fb',q).textContent='Oplossing getoond.';$('.fb',q).className='fb'});
    }else if(type==='fill'){
      var re=new RegExp(q.dataset.pattern,q.dataset.flags||''),inp=$('input',q),fb=$('.fb',q);
      var check=function(){var v=inp.value.trim().replace(/\s+/g,' ');var okk=re.test(v);var f=$('.fill',q);
        f.classList.remove('good','fail');f.classList.add(okk?'good':'fail');q.classList.remove('ok','bad');q.classList.add(okk?'ok':'bad');
        fb.className='fb '+(okk?'ok':'bad');fb.textContent=okk?'Juist!':'Niet juist. Probeer opnieuw of bekijk het antwoord.';score()};
      $('.check',q).addEventListener('click',check);
      inp.addEventListener('keydown',function(e){if(e.key==='Enter')check()});
      $('.show',q).addEventListener('click',function(){fb.className='fb';fb.innerHTML='Antwoord: <span class="answer"></span>';$('.answer',fb).textContent=q.dataset.answer});
    }
  });
  $('.quizreset',pg).addEventListener('click',function(){qs.forEach(function(q){q.classList.remove('ok','bad');$$('.opt',q).forEach(function(x){x.disabled=false;x.classList.remove('right','wrong')});var ex=$('.explain',q);if(ex)ex.hidden=true;$$('.matchrow',q).forEach(function(r){r.classList.remove('good','fail');$('select',r).selectedIndex=0;$('.mark',r).textContent=''});var f=$('.fill',q);if(f){f.classList.remove('good','fail');$('input',f).value=''}var fb=$('.fb',q);if(fb){fb.textContent='';fb.className='fb'}});score()});
  score();
});

/* zoeken */
var IDX=null,sel=-1;
function buildIdx(){
  IDX=[];var cnt=0;
  var tabLabel=function(num,k){var a=$('nav.tabs[data-chap="'+num+'"] a[href="#'+num+'/'+k+'"]');return a?a.textContent.trim():k};
  $$('.page').forEach(function(p){
    var pid=p.dataset.pid;if(pid==='home')return;
    var num=pid.split('-')[0],k=pid.slice(3);
    var ct=$('#chpanel a[href^="#'+num+'/"]');var chTitle=ct?ct.textContent.replace(/^\d+/,'').trim():num;
    $$('.sec,.ex,.q,.pdfgrid .pdfcard,.setintro',p).forEach(function(b){
      if(!b.id)b.id='sx'+(cnt++);
      var cl=b.cloneNode(true);$$('details.solution,.explain,button,select,script,.num,.n,.badge,.exctl,.tag',cl).forEach(function(x){x.parentNode.removeChild(x)});
      var text=cl.textContent.replace(/\s+/g,' ').trim();if(!text)return;
      var hd=$('h2',cl)||$('.qt',cl)||$('b',cl);
      var head=hd?hd.textContent.replace(/\s+/g,' ').trim():'';
      IDX.push({num:num,k:k,id:b.id,head:head,text:text,low:(head+' '+text).toLowerCase(),where:num+' '+chTitle+' › '+tabLabel(num,k)});
    });
  });
}
function openSearch(){if(!IDX)buildIdx();$('#searchov').hidden=false;var i=$('#searchin');i.value='';i.focus();$('#searchres').innerHTML='';sel=-1}
function closeSearch(){$('#searchov').hidden=true}
$('#searchbtn').addEventListener('click',openSearch);
$('#searchov').addEventListener('click',function(e){if(e.target===this)closeSearch()});
document.addEventListener('keydown',function(e){
  var tag=(e.target.tagName||'').toLowerCase();
  if(e.key==='Escape'){closeSearch();$('#lightbox').hidden=true}
  if(((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='k')||(e.key==='/'&&tag!=='input'&&tag!=='textarea'&&tag!=='select')){e.preventDefault();openSearch()}
});
function doSearch(){
  var q=$('#searchin').value.trim().toLowerCase(),box=$('#searchres');sel=-1;
  if(q.length<2){box.innerHTML='';return}
  var words=q.split(/\s+/).filter(Boolean),res=[];
  IDX.forEach(function(it){
    var s=0;for(var i=0;i<words.length;i++){var p=it.low.indexOf(words[i]);if(p<0){s=-1;break}s+=1+(it.head.toLowerCase().indexOf(words[i])>=0?5:0)}
    if(s>=0)res.push({it:it,s:s})
  });
  res.sort(function(a,b){return b.s-a.s});res=res.slice(0,30);
  if(!res.length){box.innerHTML='<div class="noresult">Geen resultaten voor “'+esc(q)+'”.</div>';return}
  box.innerHTML=res.map(function(r){
    var it=r.it,t=it.text,p=t.toLowerCase().indexOf(words[0]);var st=Math.max(0,p-50);var sn=t.substr(st,170);
    var h=esc(sn);words.forEach(function(w){h=h.replace(new RegExp('('+w.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+')','ig'),'<mark>$1</mark>')});
    return '<a href="#'+it.num+'/'+it.k+'" data-id="'+it.id+'"><b>'+esc(it.head||it.where)+'</b><small>'+esc(it.where)+'</small>'+(st>0?'…':'')+h+'…</a>';
  }).join('');
}
$('#searchin').addEventListener('input',doSearch);
$('#searchin').addEventListener('keydown',function(e){
  var items=$$('#searchres a');if(!items.length)return;
  if(e.key==='ArrowDown'||e.key==='ArrowUp'){e.preventDefault();sel=(sel+(e.key==='ArrowDown'?1:-1)+items.length)%items.length;items.forEach(function(a,i){a.classList.toggle('sel',i===sel)});items[sel].scrollIntoView({block:'nearest'})}
  if(e.key==='Enter'){e.preventDefault();(items[sel>=0?sel:0]).click()}
});
$('#searchres').addEventListener('click',function(e){
  var a=e.target.closest('a');if(!a)return;
  pendingAnchor=a.dataset.id;closeSearch();
  if(location.hash===a.getAttribute('href'))show();
});

/* print: alles openen (alleen ontgrendelde sets) */
window.addEventListener('beforeprint',function(){$$('details').forEach(function(d){var s=d.closest('.exset');if(!s||s.classList.contains('unlocked'))d.open=true})});

homeUpdate();show();scrollSpy();
})();
