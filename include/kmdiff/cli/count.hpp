/*****************************************************************************
 *   kmdiff
 *   Authors: T. Lemane
 *
 *  This program is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU Affero General Public License as
 *  published by the Free Software Foundation, either version 3 of the
 *  License, or (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU Affero General Public License for more details.
 *
 *  You should have received a copy of the GNU Affero General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *****************************************************************************/

#pragma once
// std
#include <memory>

// ext
#include <bcli/bcli.hpp>

// int
#include <kmdiff/cli/cli_common.hpp>
#include <kmdiff/cmd/count.hpp>
#include <kmdiff/config.hpp>
#define _KM_LIB_INCLUDE_
#include <kmtricks/utilities.hpp>

namespace kmdiff
{
kmdiff_options_t count_cli(std::shared_ptr<bc::Parser<1>> cli, count_options_t options);

};  // namespace kmdiff