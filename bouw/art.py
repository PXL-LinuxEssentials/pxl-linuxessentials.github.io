# Originele hero-illustraties (inline SVG), wit/transparant op de gradient van de hero
S='fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"'
F='fill="rgba(255,255,255,.22)" stroke="#fff" stroke-width="3" stroke-linejoin="round"'
A='fill="#fde68a"'
def win(inner):
    return ('<rect x="14" y="14" width="212" height="132" rx="12" %s/><path d="M14 38h212" %s/>'
            '<circle cx="30" cy="26" r="4" fill="#fca5a5"/><circle cx="44" cy="26" r="4" fill="#fde68a"/><circle cx="58" cy="26" r="4" fill="#86efac"/>' % (F, S)) + inner
ART = {
'01': '<circle cx="120" cy="80" r="56" %s/><ellipse cx="120" cy="80" rx="24" ry="56" %s/><path d="M64 80h112M74 52h92M74 108h92" %s/><circle cx="64" cy="80" r="7" %s/><circle cx="176" cy="80" r="7" %s/><circle cx="120" cy="24" r="7" %s/><circle cx="120" cy="136" r="7" %s/>' % (F,S,S,A,A,A,A),
'02': '<rect x="44" y="20" width="90" height="30" rx="7" %s/><rect x="44" y="58" width="90" height="30" rx="7" %s/><rect x="44" y="96" width="90" height="30" rx="7" %s/><circle cx="62" cy="35" r="4" %s/><circle cx="62" cy="73" r="4" %s/><circle cx="62" cy="111" r="4" %s/><path d="M170 120a22 22 0 0 1 4-43 30 30 0 0 1 56 8 18 18 0 0 1-2 35z" %s/><path d="M200 112V92m-9 8 9-9 9 9" %s/>' % (F,F,F,A,A,A,F,S),
'03': win('<path d="M34 62l14 10-14 10" %s/><path d="M58 84h30" %s/><path d="M34 112h110" stroke="#fff" stroke-opacity=".5" stroke-width="3" stroke-linecap="round"/><rect x="100" y="64" width="12" height="22" %s/>' % (S,S,A)),
'04': '<rect x="30" y="20" width="62" height="38" rx="6" %s/><path d="M61 58v62M61 82h40M61 120h40" %s/><rect x="101" y="68" width="56" height="30" rx="6" %s/><rect x="101" y="106" width="56" height="30" rx="6" %s/><path d="M176 84h40M176 122h40" stroke="#fff" stroke-opacity=".6" stroke-width="3" stroke-linecap="round"/>' % (F,S,F,F),
'05': '<path d="M60 56l60-28 60 28v62l-60 28-60-28z" %s/><path d="M60 56l60 28 60-28M120 84v62" %s/><path d="M96 42l60 28v26" %s/><path d="M200 24v26m-10-10 10 10 10-10" stroke="#fde68a" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>' % (F,S,S),
'06': '<path d="M52 18h84l32 32v92H52z" %s/><path d="M136 18v32h32" %s/><path d="M70 66h60M70 84h80M70 102h50M70 120h66" %s/><circle cx="170" cy="112" r="22" %s/><path d="M186 128l24 22" %s/>' % (F,S,S,F,S),
'07': '<rect x="14" y="56" width="62" height="44" rx="8" %s/><rect x="164" y="56" width="62" height="44" rx="8" %s/><path d="M76 78h88m-12-12 12 12-12 12" %s/><path d="M110 40v76" stroke="#fde68a" stroke-width="5" stroke-linecap="round"/><path d="M28 78h34M178 78h34" %s/>' % (F,F,S,S),
'08': '<path d="M30 28h180L140 88v46l-40 14V88z" %s/><path d="M54 14v8M90 12v10M130 14v8M170 12v10" %s/><path d="M100 104h40" %s/><circle cx="120" cy="120" r="5" %s/>' % (F,S,S,A),
'09': '<circle cx="120" cy="52" r="22" %s/><path d="M76 134a44 44 0 0 1 88 0z" %s/><circle cx="52" cy="70" r="15" %s/><path d="M22 128a30 30 0 0 1 56-8" %s/><circle cx="188" cy="70" r="15" %s/><path d="M218 128a30 30 0 0 0-56-8" %s/>' % (F,F,F,S,F,S),
'10': '<rect x="64" y="66" width="112" height="78" rx="12" %s/><path d="M88 66V48a32 32 0 0 1 64 0v18" %s/><circle cx="120" cy="100" r="9" %s/><path d="M120 108v14" %s/>' % (F,S,A,S),
'11': '<circle cx="86" cy="82" r="34" %s/><circle cx="86" cy="82" r="11" %s/><path d="M86 38v10M86 116v10M42 82h10M120 82h10M55 51l7 7M110 106l7 7M55 113l7-7M110 58l7-7" %s/><circle cx="176" cy="96" r="38" %s/><path d="M176 70v26l18 12" %s/>' % (F,S,S,F,S),
'12': '<path d="M120 20l14 38 40 4-31 26 10 40-33-22-33 22 10-40-31-26 40-4z" %s/><path d="M200 24v22M189 35h22M40 100v18M31 109h18" %s/><circle cx="210" cy="112" r="5" %s/>' % (F,S,A),
}
def hero_art(num):
    return '<svg class="heroart" viewBox="0 0 240 160" aria-hidden="true">%s</svg>' % ART[num]
def card_art(num):
    return hero_art(num).replace('heroart','cardart')
