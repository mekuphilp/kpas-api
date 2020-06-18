<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Skole extends Model
{
    //
    public $incrementing = false;
    protected $primaryKey = 'NSRId';
    protected $fillable = ['Kommunenr', 'Navn', 'OrgNr', 'NSRId','ErSkole', 'ErSkoleEier', 'ErGrunnSkole', 'ErPrivatSkole','ErOffentligSkole', 'ErVideregaaendeSkole'];
}