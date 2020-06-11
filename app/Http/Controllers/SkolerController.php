<?php

namespace App\Http\Controllers;

use App\Filker;
use App\Kommune;
use App\Skole;
use Illuminate\Database\Eloquent\Collection;
use Illuminate\Http\Request;

class SkolerController extends Controller
{
    /**
     * @return Filker[]|Collection
     */
    public function all_filke()
    {
        return Filker::all()->sortBy('Navn');
    }
    /**
     * @return Kommune[]|Collection
     */
    public function all_kommune()
    {
        return Kommune::all()->sortBy('Navn');
    }
    /**
     * @return Skole[]|Collection
     */
    public function all_skole()
    {
        return Skole::where('ErSkole', true)->orderBy('Navn', 'ASC')->get();
    }
    /**
     * Kommuner i Filke
     * @param string $fylkesnr
     * @return Kommune[]|Collection
     */
    public function kommuner(string $fylkesnr)
    {
        $kommuner = Kommune::where('Fylkesnr', $fylkesnr);
        return $kommuner->orderBy('Navn', 'ASC')->get();
    }

    /**
     * skoler i kommune
     *
     * @param string $kommunenr
     * @return Skole[]|Collection
     */
    public function skoler(string $kommunenr)
    {
        $skoler = Skole::where('ErSkole', true)->where("Kommunenr", $kommunenr);
        return $skoler->orderBy('Navn', 'ASC')->get();
    }

    /**
     *  Post Filke
     * @param Request $request
     * @return Filker
     */
    public function store_fylke(Request $request)
    {
        return Filker::updateOrCreate($request->all())->get();

    }

    /**
     *  Post Kommune
     * @param Request $request
     * @return Filker
     */
    public function store_kommune(Request $request)
    {
        return Kommune::updateOrCreate($request->all())->get();

    }

    /**
     *  Post Skole
     * @param Request $request
     * @return Skole
     */
    public function store_skole(Request $request)
    {
        return Skole::updateOrCreate($request->all())->get();

    }
}
