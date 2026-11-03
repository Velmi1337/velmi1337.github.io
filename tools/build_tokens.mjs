// SPDX-License-Identifier: GPL-3.0-only
import { Hct, SchemeTonalSpot, TonalPalette, argbFromHex, hexFromArgb } from '@material/material-color-utilities';
import fs from 'node:fs';
const colors={lavender:'#6750A4',mint:'#006C4C',sky:'#00639B',rose:'#984061'};
const roles=['primary','onPrimary','primaryContainer','onPrimaryContainer','secondary','onSecondary','secondaryContainer','onSecondaryContainer','tertiary','onTertiary','tertiaryContainer','onTertiaryContainer','error','onError','errorContainer','onErrorContainer','surface','surfaceDim','surfaceBright','surfaceContainerLowest','surfaceContainerLow','surfaceContainer','surfaceContainerHigh','surfaceContainerHighest','onSurface','onSurfaceVariant','outline','outlineVariant','inverseSurface','inverseOnSurface','inversePrimary','scrim','shadow'];
const kebab=s=>s.replace(/[A-Z]/g,c=>'-'+c.toLowerCase());
const palette=(seed,dark)=>{
 const scheme=new SchemeTonalSpot(Hct.fromInt(argbFromHex(seed)),dark,0);
 const result=Object.fromEntries(roles.map(r=>['--md-sys-color-'+kebab(r),hexFromArgb(scheme[r])]));
 for(const [name,value] of Object.entries({ctsv:'#006C4C',alol:'#8F4F24'})){
  const p=TonalPalette.fromInt(argbFromHex(value));
  result['--'+name+'-container']=hexFromArgb(p.tone(dark?30:90));
  result['--on-'+name+'-container']=hexFromArgb(p.tone(dark?90:10));
 }
 return Object.entries(result).map(([k,v])=>`  ${k}: ${v};`).join('\n');
};
let css='/* Generated from Google Material Color Utilities, SchemeTonalSpot. Do not edit tokens by hand. */\n';
for(const [name,seed] of Object.entries(colors)){
 const sel=name==='lavender'?`html:not([data-palette]), html[data-palette="${name}"]`:`html[data-palette="${name}"]`;
 css+=`${sel}{\n${palette(seed,false)}\n}\n`;
 const selections=sel.split(', ').map(s=>s+'[data-mode="dark"]');
 css+=`${selections.join(', ')}{\n${palette(seed,true)}\n}\n`;
 css+=`@media(prefers-color-scheme:dark){${sel.split(', ').map(s=>s+':not([data-mode="light"]):not([data-mode="dark"])').join(', ')}{\n${palette(seed,true)}\n}}\n`;
}
fs.writeFileSync('assets/tokens.css',css);
console.log('Generated M3 color roles: 4 palettes × light/dark');
